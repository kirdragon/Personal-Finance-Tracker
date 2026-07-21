from database import Database
from transaction import Transaction

class Manager:
    def __init__(self):
        self.database = Database()
        
    def income(self, amount):
        transaction = Transaction("income",amount)
        self.database.add_transaction(transaction)
        
    def expense(self,amount):
        transaction = Transaction("expense",amount)
        self.database.add_transaction(transaction)
        
    def delete(self,index):
        self.database.delete_transaction(index)
        
    def show(self):
        return self.database.show_transactions()