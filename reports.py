import sqlite3


# View all products
def view_all_products():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    if products:

        print("\n===== ALL PRODUCTS =====\n")

        for product in products:
            print("Product ID :", product[0])
            print("Name       :", product[1])
            print("Category   :", product[2])
            print("Price      :", product[3])
            print("Quantity   :", product[4])
            print("Supplier ID:", product[5])
            print("-" * 30)

    else:
        print("No Products Found!")

    conn.close()


# Low stock alert
def low_stock_alert():

    limit = int(input("Enter Low Stock Limit: "))

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM products
        WHERE quantity < ?
        """,
        (limit,)
    )

    products = cursor.fetchall()

    if products:

        print("\n===== LOW STOCK PRODUCTS =====\n")

        for product in products:
            print("Product ID :", product[0])
            print("Name       :", product[1])
            print("Quantity   :", product[4])
            print("-" * 30)

    else:
        print("No Low Stock Products Found!")

    conn.close()


# Total purchases report
def total_purchases():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(quantity)
        FROM purchases
        """
    )

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\nTotal Purchased Quantity:", total)

    conn.close()


# Total sales report
def total_sales():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(quantity)
        FROM sales
        """
    )

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\nTotal Sold Quantity:", total)

    conn.close()


# Reports Menu
while True:

    print("\n===== REPORT MENU =====")
    print("1. View All Products")
    print("2. Low Stock Alert")
    print("3. Total Purchases")
    print("4. Total Sales")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_products()

    elif choice == "2":
        low_stock_alert()

    elif choice == "3":
        total_purchases()

    elif choice == "4":
        total_sales()

    elif choice == "5":
        print("Exiting Reports Module...")
        break

    else:
        print("Invalid Choice! Please try again.")