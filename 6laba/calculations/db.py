import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("calculations.db")
        self.create_table()
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                data TEXT,
                area REAL,
                heat REAL,
                time TEXT
            )
        """)
        self.conn.commit()
    
    def save(self, type, data, area, heat):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO results (type, data, area, heat, time)
            VALUES (?, ?, ?, ?, ?)
        """, (type, data, area, heat, datetime.now().strftime("%H:%M:%S")))
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM results ORDER BY id DESC")
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()

db = Database()