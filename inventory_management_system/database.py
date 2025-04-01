import sqlite3
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO)

def connect_db():
    try:
        conn = sqlite3.connect('inventory.db')
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        return None

def create_tables():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                brand TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        conn.commit()
        conn.close()
    else:
        logging.error("Failed to create tables due to database connection error.")
