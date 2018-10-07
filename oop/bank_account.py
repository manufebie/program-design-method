'''
- Create account
- Deposit money
- Withdraw money
- Display balance
'''

class BankAccount:
    # class variables
    bank_name = 'Hogwartz Finances'
    accounts = 0

    # constractors -> values differ from each instance
    # All accounts starts with the same balace -> 0.00
    def __init__(self, firstname, lastname, balance=0.00):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

        BankAccount.accounts += 1

    @property # to get atrribute value
    def account_detail(self):
        '''
        Return the account holder detail
        
        '''
        return 'Account holder: {} {}\nBalance: {}'.format(self.firstname, self.lastname, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount

    


