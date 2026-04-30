import time
import random
from datetime import datetime, timedelta
from scrapers.lider import LiderScraper
from notifier import enviar_alerta_telegram
from db.manager import DatabaseManager
from logger import setup_logger

# Inicializamos el gestor de base de datos y el logger
db = DatabaseManager()
logger = setup_logger()

# Configuración de categorías a scrapear de Lider
CATEGORIAS_LIDER = [
    {"nombre": "Lider - TVs", "cat_id": "66849718_44699651", "sort": "best_match"},
    {"nombre": "Lider - Consolas", "cat_id": "66849718_80980590_45869788", "sort": "best_match"},
    {"nombre": "Lider - Smartphones", "cat_id": "34388900_60412644_48497435", "sort": "best_match"},
    {"nombre": "Lider - Notebooks", "cat_id": "89057520_72573679_94067303", "sort": "best_match"},
    {"nombre": "Lider - Tablets", "cat_id": "89057520_72573679_62826909", "sort": "best_match"}
]

# Configuración de tiempo
INTERVALO_MINUTOS = 15

def revisar_tienda(store_config):
    # Aseguramos que el logger use el archivo del día actual
    global logger
    logger = setup_logger()
    
    store_name = store_config["nombre"]
    cat_id = store_config["cat_id"]
    sort = store_config["sort"]
    
    ultima_vez = db.get_last_execution(store_name)
    if ultima_vez:
        tiempo_pasado = datetime.now() - ultima_vez
        if tiempo_pasado < timedelta(minutes=INTERVALO_MINUTOS):
            minutos_restantes = INTERVALO_MINUTOS - (tiempo_pasado.total_seconds() / 60)
            logger.info(f"[WAIT] {store_name}: Proximo escaneo en {minutos_restantes:.1f} min.")
            return

    scraper = LiderScraper(cat_id=cat_id, sort=sort)
    productos = scraper.scrape()
    
    if not productos:
        logger.info(f"[SKIP] {store_name}: No se obtuvieron productos.")
        return

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
        # Mezclamos las categorías para que no siempre se escaneen en el mismo orden
        categorias_shuffled = CATEGORIAS_LIDER.copy()
        random.shuffle(categorias_shuffled)
        
        for config in categorias_shuffled:
            try:
                revisar_tienda(config)
                # Pausa aleatoria entre categorías (entre 10 y 30 segundos)
                time.sleep(random.uniform(10, 30))
            except Exception as e:
                logger.error(f"Error al revisar {config['nombre']}: {e}")
        
        # Intervalo con "jitter" (variación aleatoria de +/- 2 minutos)
        jitter = random.uniform(-2, 2)
        espera_final = max(1, (INTERVALO_MINUTOS + jitter))
        logger.info(f"Ciclo completado. Durmiendo {espera_final:.1f} minutos...")
        time.sleep(espera_final * 60)