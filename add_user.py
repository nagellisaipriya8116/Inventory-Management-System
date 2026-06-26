import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

users = [
    ("admin", "1234"),
    ("sai", "abcd"),
    ("ram", "5678")
]

cursor.executemany(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    users
)

conn.commit()
conn.close()

print("Users added successfully!")