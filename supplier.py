import sqlite3


def add_supplier():
    supplier_name = input("Enter Supplier Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO suppliers (supplier_name, phone, address)
        VALUES (?, ?, ?)
        """,
        (supplier_name, phone, address)
    )

    conn.commit()
    conn.close()

    print("Supplier Added Successfully!")


def view_suppliers():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()

    if suppliers:
        print("\n===== SUPPLIER LIST =====\n")

        for supplier in suppliers:
            print("Supplier ID   :", supplier[0])
            print("Supplier Name :", supplier[1])
            print("Phone         :", supplier[2])
            print("Address       :", supplier[3])
            print("-" * 30)
    else:
        print("No suppliers found!")

    conn.close()


def search_supplier():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    supplier_name = input("Enter Supplier Name to Search: ")

    cursor.execute(
        "SELECT * FROM suppliers WHERE supplier_name = ?",
        (supplier_name,)
    )

    supplier = cursor.fetchone()

    if supplier:
        print("\n===== SUPPLIER FOUND =====\n")
        print("Supplier ID   :", supplier[0])
        print("Supplier Name :", supplier[1])
        print("Phone         :", supplier[2])
        print("Address       :", supplier[3])
    else:
        print("Supplier Not Found!")

    conn.close()


def update_supplier():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    supplier_id = int(input("Enter Supplier ID to Update: "))
    new_phone = input("Enter New Phone Number: ")
    new_address = input("Enter New Address: ")

    cursor.execute(
        """
        UPDATE suppliers
        SET phone = ?, address = ?
        WHERE supplier_id = ?
        """,
        (new_phone, new_address, supplier_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Supplier Updated Successfully!")
    else:
        print("Supplier ID Not Found!")

    conn.close()


def delete_supplier():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    supplier_id = int(input("Enter Supplier ID to Delete: "))

    cursor.execute(
        "DELETE FROM suppliers WHERE supplier_id = ?",
        (supplier_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Supplier Deleted Successfully!")
    else:
        print("Supplier ID Not Found!")

    conn.close()


while True:
    print("\n===== SUPPLIER MENU =====")
    print("1. Add Supplier")
    print("2. View Suppliers")
    print("3. Search Supplier")
    print("4. Update Supplier")
    print("5. Delete Supplier")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_supplier()

    elif choice == "2":
        view_suppliers()

    elif choice == "3":
        search_supplier()

    elif choice == "4":
        update_supplier()

    elif choice == "5":
        delete_supplier()

    elif choice == "6":
        print("Exiting Supplier Module...")
        break

    else:
        print("Invalid Choice! Please try again.")