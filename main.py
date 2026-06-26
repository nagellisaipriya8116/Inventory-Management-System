import os

# Change working directory to the folder where main.py is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Product Module")
    print("2. Supplier Module")
    print("3. Purchase Module")
    print("4. Sales Module")
    print("5. Reports Module")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("python product.py")

    elif choice == "2":
        os.system("python supplier.py")

    elif choice == "3":
        os.system("python purchase.py")

    elif choice == "4":
        os.system("python sales.py")

    elif choice == "5":
        os.system("python reports.py")

    elif choice == "6":
        print("Thank You For Using Inventory Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")