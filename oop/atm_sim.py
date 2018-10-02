'''
- Create account
- Deposit money
- Withdraw money
- Display balance
'''

class BankAccount:
    # class variables
    bank_name = 'Hogwartz Finances'

    # constractors -> values differ from each instance
    # All accounts starts with the same balace -> 0.00
    def __init__(self, firstname, lastname, balance=0.00):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

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

    

# accounts
account1 = BankAccount('John', 'Doe')
account2 = BankAccount('Jane', 'Doe')
account3 = BankAccount('Test', 'User')

#account1.deposit(1000)
account3.deposit(2000)
print(account3.account_detail)
account3.withdraw(1000)

#print(account1.account_detail)
#print()
print(account3.account_detail)
