import sqlite3

def low_stock_alert():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM products
        WHERE quantity < 10
        """
    )

    products = cursor.fetchall()

    if products:

        print("\n===== LOW STOCK ALERT =====\n")

        for product in products:
            print("Product ID :", product[0])
            print("Name       :", product[1])
            print("Category   :", product[2])
            print("Price      :", product[3])
            print("Quantity   :", product[4])
            print("-" * 30)

    else:
        print("No Low Stock Products Found!")

    conn.close()


low_stock_alert()