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
                                    transaction_type TEXT,
                                    amount REAL
                                    )""")
        self.connection.commit()
    
    def add_transaction(self, transaction):
        self.cursor.execute("""
                    INSERT INTO transactions(transaction_type, amount)
                    VALUES (?, ?)""",(transaction.type, transaction.amount))
        
        self.connection.commit()
    
    def delete_transaction(self,index):
        self.cursor.execute("""
                            DELETE FROM transactions
                            WHERE id = ?;
                            """,(index,))
        
        self.connection.commit()
        
    def show_transactions(self):
        self.cursor.execute("""
                            SELECT * FROM transactions;
                            """)
        rows = self.cursor.fetchall()
        
        return rows
    
    def transaction_exists(self,id):
        self.cursor.execute("""
                            SELECT * FROM transactions
                            WHERE id = ?;
                            """,(id,))
        if self.cursor.fetchall():
            return True
        else:
            return False
    def change_transaction(self,id, type,amount):
        self.cursor.execute("""
                            UPDATE transactions
                            SET transaction_type = ?,
                                amount = ?
                            WHERE id = ?;
                            """,(type,amount,id))
    def close(self):
        self.connection.close()