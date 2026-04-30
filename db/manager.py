import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="rata_bot.db"):
        self.db_path = os.path.join("db", db_name)
        self._init_db()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Table for stores
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS stores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            ''')
            
            # Table for products
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    store_id INTEGER NOT NULL,
                    external_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    url TEXT NOT NULL,
                    category TEXT,
                    seller TEXT,
                    FOREIGN KEY (store_id) REFERENCES stores (id),
                    UNIQUE(store_id, external_id)
                )
            ''')
            
            # Table for price history
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS price_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    price INTEGER NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
            ''')

            # Table for store execution logs
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scrape_logs (
                    store_id INTEGER PRIMARY KEY,
                    last_execution DATETIME,
                    FOREIGN KEY (store_id) REFERENCES stores (id)
                )
            ''')
            conn.commit()

    def get_or_create_store(self, name):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO stores (name) VALUES (?)", (name,))
            cursor.execute("SELECT id FROM stores WHERE name = ?", (name,))
            return cursor.fetchone()[0]

    def save_products(self, store_name, products_data):
        store_id = self.get_or_create_store(store_name)
        changes_detected = False
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            for p in products_data:
                external_id = str(p.get("external_id"))
                name = p.get("name")
                url = p.get("url")
                category = p.get("category")
                seller = p.get("seller")
                price = p.get("price")

                # Insert or update product
                cursor.execute('''
                    INSERT INTO products (store_id, external_id, name, url, category, seller)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(store_id, external_id) DO UPDATE SET
                        name = excluded.name,
                        url = excluded.url,
                        category = excluded.category,
                        seller = excluded.seller
                ''', (store_id, external_id, name, url, category, seller))

                # Get the internal product id
                cursor.execute("SELECT id FROM products WHERE store_id = ? AND external_id = ?", (store_id, external_id))
                product_id = cursor.fetchone()[0]

                # Save price if it changed or if it's the first time
                cursor.execute('''
                    SELECT price FROM price_history 
                    WHERE product_id = ? 
                    ORDER BY timestamp DESC LIMIT 1
                ''', (product_id,))
                last_price_row = cursor.fetchone()
                
                if not last_price_row or last_price_row[0] != price:
                    changes_detected = True
                    cursor.execute('''
                        INSERT INTO price_history (product_id, price)
                        VALUES (?, ?)
                    ''', (product_id, price))
            
            conn.commit()
        return changes_detected

    def get_price_stats(self, store_name, external_id):
        """Devuelve el precio anterior y el precio mínimo histórico."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Obtener ID interno
            cursor.execute('''
                SELECT p.id FROM products p
                JOIN stores s ON p.store_id = s.id
                WHERE s.name = ? AND p.external_id = ?
            ''', (store_name, str(external_id)))
            row = cursor.fetchone()
            if not row:
                return None
            
            product_id = row[0]
            
            # Precio anterior (el segundo más reciente)
            cursor.execute('''
                SELECT price FROM price_history 
                WHERE product_id = ? 
                ORDER BY timestamp DESC LIMIT 1 OFFSET 1
            ''', (product_id,))
            prev_row = cursor.fetchone()
            prev_price = prev_row[0] if prev_row else None
            
            # Precio mínimo histórico anterior (excluyendo el registro actual que acaba de ser insertado)
            cursor.execute('''
                SELECT MIN(price) FROM price_history 
                WHERE product_id = ? AND timestamp < (SELECT MAX(timestamp) FROM price_history WHERE product_id = ?)
            ''', (product_id, product_id))
            min_row = cursor.fetchone()
            min_price = min_row[0] if min_row else None
            
            return {
                "previous_price": prev_price,
                "min_historical": min_price
            }

    def get_last_execution(self, store_name):
        """Devuelve el datetime de la última ejecución para una tienda."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT last_execution FROM scrape_logs sl
                JOIN stores s ON sl.store_id = s.id
                WHERE s.name = ?
            ''', (store_name,))
            row = cursor.fetchone()
            if row and row[0]:
                return datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            return None

    def update_last_execution(self, store_name):
        """Actualiza la fecha de última ejecución a ahora."""
        store_id = self.get_or_create_store(store_name)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO scrape_logs (store_id, last_execution)
                VALUES (?, ?)
                ON CONFLICT(store_id) DO UPDATE SET last_execution = excluded.last_execution
            ''', (store_id, now))
            conn.commit()

    def cleanup_old_prices(self):
        """Elimina registros de más de 3 meses, conservando el precio mínimo y el último para cada producto."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Obtener todos los productos
            cursor.execute("SELECT id FROM products")
            products = cursor.fetchall()
            
            total_deleted = 0
            for (p_id,) in products:
                # Identificar el ID del precio mínimo histórico
                cursor.execute('''
                    SELECT id FROM price_history 
                    WHERE product_id = ? 
                    ORDER BY price ASC, timestamp ASC LIMIT 1
                ''', (p_id,))
                min_row = cursor.fetchone()
                
                # Identificar el ID del último precio registrado
                cursor.execute('''
                    SELECT id FROM price_history 
                    WHERE product_id = ? 
                    ORDER BY timestamp DESC LIMIT 1
                ''', (p_id,))
                last_row = cursor.fetchone()
                
                keep_ids = set()
                if min_row: keep_ids.add(min_row[0])
                if last_row: keep_ids.add(last_row[0])
                
                if not keep_ids:
                    continue
                
                # Borrar registros antiguos que no sean el mínimo ni el último
                placeholders = ','.join(['?'] * len(keep_ids))
                cursor.execute(f'''
                    DELETE FROM price_history 
                    WHERE product_id = ? 
                    AND timestamp < date('now', '-3 months')
                    AND id NOT IN ({placeholders})
                ''', (p_id, *list(keep_ids)))
                total_deleted += cursor.rowcount
            
            conn.commit()
            return total_deleted
