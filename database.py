import sqlite3

# Connect to database (creates inventory.db if it doesn't exist)
conn = sqlite3.connect("inventory.db")

# Create cursor
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Create Suppliers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL,
    phone TEXT,
    address TEXT
)
""")

# Create Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    price REAL,
    quantity INTEGER,
    supplier_id INTEGER
)
""")

# Create Purchases Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    purchase_date TEXT
)
""")

# Create Sales Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    sale_date TEXT
)
""")

# Save changes
conn.commit()

import os

print("Database location:")
print(os.path.abspath("inventory.db"))

# Close connection
conn.close()

print("Database and tables created successfully!")