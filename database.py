
import sqlite3

# Connect to database
def connect_db():
    con = sqlite3.connect("shop.db")
    return con


# Create product and order tables
def create_tables():

    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            price REAL,
            stock INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            total REAL
        )
    """)

    con.commit()
    con.close()


# Insert sample products
def add_products():

    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM products")
    count = cur.fetchone()[0]

    if count == 0:

        products = [
            ("Laptop", "Electronics", 45000, 10),
            ("Mobile", "Electronics", 18000, 15),
            ("Headphones", "Accessories", 1500, 20),
            ("Keyboard", "Accessories", 800, 25),
            ("Mouse", "Accessories", 500, 30),
            ("Smart Watch", "Electronics", 2500, 12)
        ]

        cur.executemany("""
            INSERT INTO products (name, category, price, stock)
            VALUES (?, ?, ?, ?)
        """, products)

    con.commit()
    con.close()


# Get all products
def get_products():

    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM products")

    products = cur.fetchall()

    con.close()

    return products
