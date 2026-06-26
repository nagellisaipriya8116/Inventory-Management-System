import sqlite3


def add_product():
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    supplier_id = int(input("Enter Supplier ID: "))

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (name, category, price, quantity, supplier_id)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category, price, quantity, supplier_id))

    conn.commit()
    conn.close()

    print("Product Added Successfully!")


def view_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    if products:
        print("\n===== PRODUCT LIST =====\n")

        for p in products:
            print("Product ID :", p[0])
            print("Name       :", p[1])
            print("Category   :", p[2])
            print("Price      :", p[3])
            print("Quantity   :", p[4])
            print("Supplier ID:", p[5])
            print("-" * 30)
    else:
        print("No products found!")

    conn.close()


def search_product():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    name = input("Enter Product Name to Search: ")

    cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
    product = cursor.fetchone()

    if product:
        print("\n===== PRODUCT FOUND =====\n")
        print("Product ID :", product[0])
        print("Name       :", product[1])
        print("Category   :", product[2])
        print("Price      :", product[3])
        print("Quantity   :", product[4])
        print("Supplier ID:", product[5])
    else:
        print("Product Not Found!")

    conn.close()


def update_product():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    product_id = int(input("Enter Product ID to Update: "))
    new_price = float(input("Enter New Price: "))
    new_quantity = int(input("Enter New Quantity: "))

    cursor.execute("""
        UPDATE products
        SET price = ?, quantity = ?
        WHERE product_id = ?
    """, (new_price, new_quantity, product_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Product Updated Successfully!")
    else:
        print("Product ID Not Found!")

    conn.close()


def delete_product():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    product_id = int(input("Enter Product ID to Delete: "))

    cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Product Deleted Successfully!")
    else:
        print("Product ID Not Found!")

    conn.close()


# 🔥 MENU SYSTEM
while True:
    print("\n===== PRODUCT MENU =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        print("Exiting Product Module...")
        break

    else:
        print("Invalid Choice! Try again.")
