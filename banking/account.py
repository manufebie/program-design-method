from time import sleep

class BaseAccount:
    '''Class representing a Bank account'''

    def __init__(self, balance=0.00):
        self.balance = balance

    def get_balance(self):
        return 'Current balance: {}'.format(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Not sufficient funds')
            sleep(2)
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount