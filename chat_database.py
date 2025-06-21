import sqlite3
from datetime import datetime

DB_NAME = "chatbot.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def get_user_id(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        c.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        return c.lastrowid

def save_message(user_id, role, message):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO messages (user_id, role, message, timestamp) VALUES (?, ?, ?, ?)",
              (user_id, role, message, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_messages(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT role, message, timestamp FROM messages WHERE user_id = ? ORDER BY id ASC", (user_id,))
    messages = c.fetchall()
    conn.close()
    return messages
