from tkinter import *
import os

# Change working directory to the folder where gui_main.py exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))

root = Tk()

# Window settings
root.title("Inventory Management System")
root.geometry("500x400")

# Heading
Label(
    root,
    text="Inventory Management System",
    font=("Arial", 18, "bold")
).pack(pady=20)

# Products Button
Button(
    root,
    text="Products",
    width=20,
    command=lambda: os.system("python product.py")
).pack(pady=5)

# Suppliers Button
Button(
    root,
    text="Suppliers",
    width=20,
    command=lambda: os.system("python supplier.py")
).pack(pady=5)

# Purchases Button
Button(
    root,
    text="Purchases",
    width=20,
    command=lambda: os.system("python purchase.py")
).pack(pady=5)

# Sales Button
Button(
    root,
    text="Sales",
    width=20,
    command=lambda: os.system("python sales.py")
).pack(pady=5)

# Reports Button
Button(
    root,
    text="Reports",
    width=20,
    command=lambda: os.system("python reports.py")
).pack(pady=5)

# Exit Button
Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
).pack(pady=20)

# Run application
root.mainloop()