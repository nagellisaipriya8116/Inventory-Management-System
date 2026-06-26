import sqlite3
import os

# Move to the folder where login.py exists
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Connect to database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Take input from user
username = input("Enter Username: ")
password = input("Enter Password: ")

# Check username and password
cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
)

result = cursor.fetchone()

if result:
    print("Login Successful")

    # Open Main Menu
    os.system("python main.py")

else:
    print("Invalid Username or Password")

conn.close()