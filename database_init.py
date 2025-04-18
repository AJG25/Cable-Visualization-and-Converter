# create_tables.py
import os
import sqlite3
import json
from werkzeug.security import generate_password_hash

DATABASE_FILE = "UsersDB.db"

# Example user data
user_data = [
    ("Jane Doe",  "doe.j@gmail.com",   generate_password_hash("123"), "Admin"),
    ("John Smith","smith.j@gmail.com", generate_password_hash("123"), "Data Scientist"),
    ("Sarah Lee", "lee.s@gmail.com",   generate_password_hash("123"), "Data Analyst")
]

def create_tables():
    """
    Creates/initializes the SQLite database with 'User' and 'Cables' tables.
    Inserts sample users if 'User' is empty.
    Leaves 'Cables' empty (we'll populate from a file or other script).
    """
    abs_path = os.path.abspath(DATABASE_FILE)
    print("Using database file at:", abs_path)

    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()

        # 1) Create User table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS User(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(128) NOT NULL,
                email VARCHAR(128) UNIQUE NOT NULL,
                password VARCHAR(128) NOT NULL,
                role VARCHAR(50)
            )
        """)

        # 2) Create Cables table
        #    Only store the entire FeatureCollection as TEXT
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cables(
                cable_id INTEGER PRIMARY KEY AUTOINCREMENT,
                feature_collection TEXT NOT NULL
            )
        """)

        # Insert sample users if none exist
        cursor.execute("SELECT COUNT(*) FROM User")
        if cursor.fetchone()[0] == 0:
            for user in user_data:
                cursor.execute("""
                    INSERT INTO User (name, email, password, role)
                    VALUES (?, ?, ?, ?)
                """, user)

        # Commit changes
        conn.commit()
        print("Tables created and sample data inserted (if empty).")

if __name__ == "__main__":
    create_tables()
