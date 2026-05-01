import time
import random
import signal
import sys
from datetime import datetime, timedelta
from scrapers.lider import LiderScraper
from scrapers.abcdin import AbcdinScraper
from notifier import enviar_alerta_telegram
from db.manager import DatabaseManager
from logger import setup_logger

# Inicializamos el gestor de base de datos y el logger
db = DatabaseManager()
logger = setup_logger()

def manejar_salida(sig, frame):
    logger.info("🛑 Señal de parada recibida. Cerrando RataBOT de forma segura...")
    sys.exit(0)

# Registrar señales de interrupción
signal.signal(signal.SIGINT, manejar_salida)
signal.signal(signal.SIGTERM, manejar_salida)

# Diccionario para rastrear errores consecutivos por categoría
errores_consecutivos = {}
fecha_ultima_limpieza = None

# Configuración de categorías a scrapear de Lider
CATEGORIAS_LIDER = [
    {"nombre": "Lider - TVs", "cat_id": "66849718_44699651", "sort": "best_match", "tienda": "Lider"},
    {"nombre": "Lider - Consolas", "cat_id": "66849718_80980590_45869788", "sort": "best_match", "tienda": "Lider"},
    {"nombre": "Lider - Smartphones", "cat_id": "34388900_60412644_48497435", "sort": "best_match", "tienda": "Lider"},
    {"nombre": "Lider - Notebooks", "cat_id": "89057520_72573679_94067303", "sort": "best_match", "tienda": "Lider"},
    {"nombre": "Lider - Tablets", "cat_id": "89057520_72573679_62826909", "sort": "best_match", "tienda": "Lider"}
]

# Configuración de categorías a scrapear de Abcdin
CATEGORIAS_ABCDIN = [
    {"nombre": "Abcdin - Smart TVs", "url": "https://www.abc.cl/tecnologia/televisores/smart-tv/", "tienda": "Abcdin"},
    {"nombre": "Abcdin - Smartphones", "url": "https://www.abc.cl/tecnologia/telefonia/smartphones/", "tienda": "Abcdin"},
    {"nombre": "Abcdin - Notebooks", "url": "https://www.abc.cl/tecnologia/computacion/notebooks/", "tienda": "Abcdin"}
]

TODAS_LAS_CATEGORIAS = CATEGORIAS_LIDER + CATEGORIAS_ABCDIN

# Configuración de tiempo
INTERVALO_MINUTOS = 15

def revisar_tienda(store_config):
    # Aseguramos que el logger use el archivo del día actual
    global logger
    logger = setup_logger()
    
    store_name = store_config["nombre"]
    tienda = store_config["tienda"]
    
    ultima_vez = db.get_last_execution(store_name)
    if ultima_vez:
        tiempo_pasado = datetime.now() - ultima_vez
        if tiempo_pasado < timedelta(minutes=INTERVALO_MINUTOS):
            minutos_restantes = INTERVALO_MINUTOS - (tiempo_pasado.total_seconds() / 60)
            logger.info(f"[WAIT] {store_name}: Proximo escaneo en {minutos_restantes:.1f} min.")
            return

    # Inicializamos el scraper correspondiente
    if tienda == "Lider":
        scraper = LiderScraper(cat_id=store_config["cat_id"], sort=store_config["sort"])
    elif tienda == "Abcdin":
        scraper = AbcdinScraper(category_url=store_config["url"])
    else:
        logger.error(f"Tienda desconocida: {tienda}")
        return

    productos = scraper.scrape()
    
    if not productos:
        logger.info(f"[SKIP] {store_name}: No se obtuvieron productos.")
        # Incrementamos contador de errores para esta categoría
        errores_consecutivos[store_name] = errores_consecutivos.get(store_name, 0) + 1
        
        if errores_consecutivos[store_name] == 3:
            logger.error(f"¡CRÍTICO! {store_name} ha fallado 3 veces consecutivas.")
            enviar_alerta_telegram(f"⚠️ <b>Error persistente en {store_name}</b>\nEl scraper no está devolviendo productos después de 3 intentos.")
        return

    # Si llegamos aquí, el scrape fue exitoso
    errores_consecutivos[store_name] = 0
    db.update_last_execution(store_name)
    logger.info(f"[{store_name}] Se encontraron {len(productos)} productos. Analizando...")
    
    # Guardamos y detectamos si hubo cambios de precios
    hay_cambios = db.save_products(store_name, productos)
    
    if hay_cambios:
        logger.info(f"[{store_name}] Cambio de precios detectado.")
    else:
        logger.info(f"[{store_name}] Sin cambios en los precios.")

    for p in productos:
        nombre = p.get("name")
        vendedor = p.get("seller")
        precio = p.get("price", 0)
        url = p.get("url", "")
        ext_id = p.get("external_id")

        if precio <= 0:
            continue

        stats = db.get_price_stats(store_name, ext_id)
        if not stats or not stats.get("previous_price"):
            continue

        precio_anterior = stats["previous_price"]
        
        if precio < precio_anterior:
            descuento = ((precio_anterior - precio) / precio_anterior) * 100
            
            # Regla de oro: Descuento extremo (>= 80%)
            if descuento >= 80:
                precio_formateado = f"${precio:,}".replace(',', '.')
                precio_anterior_txt = f"${precio_anterior:,}".replace(',', '.')
                
                mensaje_telegram = (
                    f"🧨 <b>¡OFERTA EXPLOSIVA DETECTADA! ({descuento:.0f}% OFF)</b> 🧨\n\n"
                    f"📺 <b>Producto:</b> {nombre}\n"
                    f"💰 <b>Precio Ahora:</b> {precio_formateado}\n"
                    f"📉 <b>Precio Antes:</b> {precio_anterior_txt}\n"
                    f"🏢 <b>Tienda:</b> {store_name}\n"
                    f"🛒 <a href='{url}'>¡CORRE POR EL TUYO!</a>"
                )
                enviar_alerta_telegram(mensaje_telegram)
                logger.info(f"[OFERTA] GANGA EN {store_name}: {nombre} ({descuento:.0f}% OFF)")

if __name__ == "__main__":
    logger.info(f"Bot de Ofertas Rata iniciado (Intervalo base: {INTERVALO_MINUTOS} min).")
    
    try:
        enviar_alerta_telegram("📡 <i>Sistema de monitoreo RataBOT sincronizado.</i>")
    except:
        pass

    while True:
        ahora = datetime.now()

        # Limpieza semanal de base de datos (Lunes a las 00:00 - 01:00)
        if ahora.weekday() == 0 and ahora.hour == 0:
            if fecha_ultima_limpieza != ahora.date():
                logger.info("Iniciando limpieza semanal de precios antiguos...")
                eliminados = db.cleanup_old_prices()
                logger.info(f"Limpieza completada. Se eliminaron {eliminados} registros antiguos.")
                fecha_ultima_limpieza = ahora.date()

        # Mezclamos las categorías para que no siempre se escaneen en el mismo orden
        categorias_shuffled = TODAS_LAS_CATEGORIAS.copy()
        random.shuffle(categorias_shuffled)
        
        for config in categorias_shuffled:
            try:
                revisar_tienda(config)
                # Pausa aleatoria entre categorías (entre 10 y 30 segundos)
                time.sleep(random.uniform(10, 30))
            except Exception as e:
                logger.error(f"Error al revisar {config['nombre']}: {e}")
                # También contamos excepciones como errores para la notificación
                name = config['nombre']
                errores_consecutivos[name] = errores_consecutivos.get(name, 0) + 1
                if errores_consecutivos[name] == 3:
                    enviar_alerta_telegram(f"❌ <b>Error crítico en {name}</b>\nSe han producido 3 excepciones seguidas: {str(e)[:100]}")
        
        # Intervalo con "jitter" (variación aleatoria de +/- 2 minutos)
        jitter = random.uniform(-2, 2)
        espera_final = max(1, (INTERVALO_MINUTOS + jitter))
        logger.info(f"Ciclo completado. Durmiendo {espera_final:.1f} minutos...")
        time.sleep(espera_final * 60)