'''

'''
from account import Account


class Customer:
    num_of_customers = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def get_account(self):
        return self.account

    def set_account(self, account):
        self.account = account  

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)
