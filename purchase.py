import sqlite3


# Function to add a purchase
def add_purchase():

    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Purchase Quantity: "))
    purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Insert purchase record
    cursor.execute(
        """
        INSERT INTO purchases
        (product_id, quantity, purchase_date)
        VALUES (?, ?, ?)
        """,
        (product_id, quantity, purchase_date)
    )

    # Increase product stock
    cursor.execute(
        """
        UPDATE products
        SET quantity = quantity + ?
        WHERE product_id = ?
        """,
        (quantity, product_id)
    )

    conn.commit()
    conn.close()

    print("Purchase Added Successfully!")
    print("Stock Updated Successfully!")


# Function to view all purchases
def view_purchases():

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM purchases")

    purchases = cursor.fetchall()

    if purchases:

        print("\n===== PURCHASE LIST =====\n")

        for purchase in purchases:
            print("Purchase ID   :", purchase[0])
            print("Product ID    :", purchase[1])
            print("Quantity      :", purchase[2])
            print("Purchase Date :", purchase[3])
            print("-" * 30)

    else:
        print("No purchases found!")

    conn.close()


# Purchase Menu
while True:

    print("\n===== PURCHASE MENU =====")
    print("1. Add Purchase")
    print("2. View Purchases")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_purchase()

    elif choice == "2":
        view_purchases()

    elif choice == "3":
        print("Exiting Purchase Module...")
        break

    else:
        print("Invalid Choice! Please try again.")