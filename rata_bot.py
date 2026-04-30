import time
from datetime import datetime, timedelta
from scrapers.lider import LiderScraper
from notifier import enviar_alerta_telegram
from db.manager import DatabaseManager

# Inicializamos el gestor de base de datos
db = DatabaseManager()

# Configuración de categorías a scrapear de Lider
CATEGORIAS_LIDER = [
    {"nombre": "Lider - TVs", "cat_id": "66849718_44699651", "sort": "best_match"},
    {"nombre": "Lider - Consolas", "cat_id": "66849718_80980590_45869788", "sort": "best_match"},
    {"nombre": "Lider - Smartphones", "cat_id": "34388900_60412644_48497435", "sort": "best_match"},
    {"nombre": "Lider - Notebooks", "cat_id": "89057520_72573679_94067303", "sort": "best_match"},
    {"nombre": "Lider - Tablets", "cat_id": "89057520_72573679_62826909", "sort": "best_match"}
]

# Configuración de tiempo
INTERVALO_MINUTOS = 30  # Escaneo cada 30 minutos (Equilibrio entre velocidad y seguridad)

def revisar_tienda(store_config):
    store_name = store_config["nombre"]
    cat_id = store_config["cat_id"]
    sort = store_config["sort"]
    
    # Verificamos si han pasado más de 30 minutos desde la última vez para ESTA categoría
    ultima_vez = db.get_last_execution(store_name)
    if ultima_vez:
        tiempo_pasado = datetime.now() - ultima_vez
        if tiempo_pasado < timedelta(minutes=INTERVALO_MINUTOS):
            minutos_restantes = INTERVALO_MINUTOS - (tiempo_pasado.total_seconds() / 60)
            print(f"[WAIT] {store_name}: Proximo escaneo en {minutos_restantes:.1f} min.")
            return

    # Inicializamos el scraper para esta categoría específica
    scraper = LiderScraper(cat_id=cat_id, sort=sort)
    productos = scraper.scrape()
    
    if not productos:
        return

    # Si hubo productos (scrape exitoso), actualizamos la fecha de ejecución
    db.update_last_execution(store_name)

    print(f"[INFO] [{store_name}] Se encontraron {len(productos)} productos. Analizando reglas...")
    
    # Guardamos todos los productos en la base de datos
    db.save_products(store_name, productos)

    for p in productos:
        nombre = p.get("name")
        vendedor = p.get("seller")
        precio = p.get("price", 0)
        url = p.get("url", "")
        ext_id = p.get("external_id")

        if precio <= 0:
            continue

        # Obtener estadísticas históricas
        stats = db.get_price_stats(store_name, ext_id)
        
        # Si no hay historial previo (producto nuevo), no alertamos
        if not stats or not stats.get("previous_price"):
            continue

        precio_anterior = stats["previous_price"]
        
        # Solo alertamos si el precio actual es menor al anterior
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
                print(f"[OFERTA] GANGA BRUTAL EN {store_name}: {nombre} ({descuento:.0f}% OFF)")

if __name__ == "__main__":
    print(f"[BOT] Bot de Ofertas Rata iniciado (Modo Servicio - Intervalo: {INTERVALO_MINUTOS} min).")

    while True:
        for config in CATEGORIAS_LIDER:
            try:
                revisar_tienda(config)
            except Exception as e:
                print(f"[ERROR] Al revisar {config['nombre']}: {e}")
        
        print(f"[SLEEP] Ciclo de escaneo completado. Durmiendo {INTERVALO_MINUTOS} minutos...")
        time.sleep(INTERVALO_MINUTOS * 60)