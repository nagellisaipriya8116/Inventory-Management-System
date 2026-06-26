import sqlite3


# Function to add a sale
def add_sale():

    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Sale Quantity: "))
    sale_date = input("Enter Sale Date (YYYY-MM-DD): ")

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Check available stock
    cursor.execute(
        "SELECT quantity FROM products WHERE product_id = ?",
        (product_id,)
    )

    result = cursor.fetchone()

    if result is None:
        print("Product ID Not Found!")
        conn.close()
        return

    current_stock = result[0]

    # Prevent overselling
    if quantity > current_stock:
        print("Insufficient Stock!")
        conn.close()
        return

    # Insert sale record
    cursor.execute(
        """
        INSERT INTO sales
        (product_id, quantity, sale_date)
        VALUES (?, ?, ?)
        """,
        (product_id, quantity, sale_date)
    )

    # Reduce stock
    cursor.execute(
        """
        UPDATE products
        SET quantity = quantity - ?
        WHERE product_id = ?
        """,
        (quantity, product_id)
    )

    conn.commit()
    conn.close()

    print("Sale Recorded Successfully!")
    print("Stock Updated Successfully!")


# Function to view all sales
def view_sales():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")

    sales = cursor.fetchall()

    if sales:

        print("\n===== SALES LIST =====\n")

        for sale in sales:
            print("Sale ID   :", sale[0])
            print("Product ID:", sale[1])
            print("Quantity  :", sale[2])
            print("Sale Date :", sale[3])
            print("-" * 30)

    else:
        print("No sales found!")

    conn.close()


# Sales Menu
while True:

    print("\n===== SALES MENU =====")
    print("1. Add Sale")
    print("2. View Sales")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_sale()

    elif choice == "2":
        view_sales()

    elif choice == "3":
        print("Exiting Sales Module...")
        break

    else:
        print("Invalid Choice! Please try again.")