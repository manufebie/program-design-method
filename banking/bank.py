from customer import Client


class Bank:
    '''Class representing a bank'''
    
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def __str__(self):
        return 'Bank name: {}'.format(name)

    def create_client(self, username, fullname):
        self.clients[username] = Client(fullname)

    def display_clients(self):
        for key, value in self.clients.items():
            return key, value