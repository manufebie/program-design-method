'''
--> Add customer
--> Get customer amount
--> Get customer
'''
from customer import Customer

class Bank:

    def __init__(self, name):
        self.name = name
        self.customers = []

        Customer.num_of_customers += 1

    def add_customer(self, firstname, lastname):
        customer = Customer(firstname, lastname)
        self.customers.append(customer)
    
    def get_customers(self): 

        for c in self.customers:
            print('{}'.format(c))



            

    
        