from account import BaseAccount


class Client(BaseAccount):
    '''Class representing a bank customer'''

    def __init__(self, fullname):
        super().__init__(balance=0.00)
        self.fullname = fullname

    def __str__(self):
        return 'Account holder: {} {}'.format(self.firstname, self.lastname)