class BankAccount:

    def __init__(self, accountID="", balance=0):
        self.accountID = accountID
        self.balance = balance

    def __str__(self):
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"
    
    def deposit(self,amount):
        self.balance += float(amount)

    def withdrawal(self, amount):
        self.balance -= float(amount)

    def set_account_ID(self, newID):
        self.accountID = newID

    def	set_balance(self, new_balance):
        self.balance = new_balance

    def get_account_ID(self):
        return f"{self.accountID}"
    
    def get_balance(self):
        return f"{self.balance:.2f}"
