class BaseScraper:
    """Interfaz mínima para un scraper.

    Implementaciones deben devolver una lista de diccionarios con al menos
    las claves: `external_id`, `name`, `seller`, `price`, `url`, `category`.
    """

    def scrape(self):
        raise NotImplementedError()
