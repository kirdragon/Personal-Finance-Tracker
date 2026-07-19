import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("operations.db")
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS transactions(
                                    id INTEGER PRIMARY KEY,
                                    category TEXT,
                                    amount REAL
                                    )""")
        self.connection.commit()