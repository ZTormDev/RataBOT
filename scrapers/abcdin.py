import requests
from bs4 import BeautifulSoup
import json
import random
import time

class AbcdinScraper:
    def __init__(self, category_url):
        self.category_url = category_url
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        ]

    def scrape(self):
        all_products = []
        # Abcdin usa el parámetro 'sz' para determinar cuántos productos mostrar. 
        # Ponemos un número alto para capturar la mayoría en una sola petición.
        url = f"{self.category_url}?sz=100"
        
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'es-CL,es;q=0.9,en;q=0.8',
            'Referer': 'https://www.abc.cl/'
        }

        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code != 200:
                return []

            soup = BeautifulSoup(response.text, 'html.parser')
            # Las tarjetas de producto tienen la clase lp-product-tile
            tiles = soup.select('.lp-product-tile')
            
            for tile in tiles:
                try:
                    # Buscamos la data estructurada en el atributo data-gtm
                    gtm_data_raw = tile.get('data-gtm')
                    if not gtm_data_raw:
                        continue
                    
                    gtm_data = json.loads(gtm_data_raw)
                    info = gtm_data.get('ecommerce', {}).get('impressions', {})
                    
                    if not info:
                        continue

                    name = info.get('name')
                    # El precio viene con puntos, ej: "289.990"
                    price_str = info.get('price', '0').replace('.', '')
                    price = int(float(price_str)) # float por si acaso, luego int
                    
                    external_id = info.get('id')
                    
                    # El link del producto está en una etiqueta <a> dentro del tile
                    link_tag = tile.select_one('a.link')
                    product_url = ""
                    if link_tag:
                        product_url = link_tag.get('href')
                        if product_url and not product_url.startswith('http'):
                            product_url = f"https://www.abc.cl{product_url}"
                    
                    brand = info.get('brand', 'Abcdin')

                    all_products.append({
                        "external_id": str(external_id),
                        "name": name,
                        "price": price,
                        "url": product_url,
                        "seller": brand,
                        "category": self.category_url.split('/')[-2] # Usamos parte del slug como categoría
                    })
                except Exception as e:
                    continue

        except Exception as e:
            print(f"❌ Error scraping Abcdin: {e}")

        return all_products
