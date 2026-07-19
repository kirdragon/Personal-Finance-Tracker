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
    
    def add_expense(self, amount):
        self.cursor.execute("""
                    INSERT INTO transactions(transaction_type, amount)
                    VALUES (?, ?)""",("expense",amount))
        
        self.connection.commit()
        
    def add_income(self,amount):
        self.cursor.execute("""
                            INSERT INTO transactions(transaction_type,amount)
                            VALUES (?, ?)""",("income",amount))
        self.connection.commit()
        
    
def delete_transaction(self,index):
        self.cursor.execute("""
                            DELETE FROM transactions
                            WHERE id = ?;
                            """,(index,))
        
        self.connection.commit()