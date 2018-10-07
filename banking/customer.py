from account import BaseAccount


class Client(BaseAccount):
    '''Class representing a bank customer'''
    total_clients = 0

    def __init__(self, fullname):
        super().__init__(balance=0.00)
        self.fullname = fullname

        Client.total_clients += 1

    def __str__(self):
        return 'Account holder: {}'.format(self.fullname)

    def display_name(self):
        return self.fullname