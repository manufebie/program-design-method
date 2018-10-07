from bank_account import BankAccount

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
print()
print('Total accounts: {}'.format(BankAccount.accounts))