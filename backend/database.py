import sqlite3

def get_connection():
    conn = sqlite3.connect("yells.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS yells (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            who_yelled TEXT NOT NULL,
            reason TEXT NOT NULL,
            count INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
