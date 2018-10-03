class Account:

    def __init__(self, balance=0.00):
        self.balance = balance

    #@property
    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
        




