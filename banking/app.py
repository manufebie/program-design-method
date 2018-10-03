'''
--> Create accounts
--> Deposit money
--> Withdraw money
--> 
'''

from account import Account
from bank import Bank
from customer import Customer

b1 = Bank('Hogwartz Finances')
b1.add_customer('Harry', 'Potter')
b1.add_customer('Hermione', 'Granger')
b1.add_customer('Albus', 'Dumbledore')

print(b1.get_customers())




