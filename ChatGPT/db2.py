import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite3 database file
DATABASE_FILE = 'student.db'

def create_database():
    if not os.path.exists(DATABASE_FILE):
        conn = sqlite3.connect(DATABASE_FILE)
        conn.close()

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# ... The rest of the code remains unchanged ...

if __name__ == '__main__':
    create_database()
    create_table()
    app.run(debug=True)
