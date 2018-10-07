'''
OOP program using static data
To run this program, run this file in your terminal.
'''
import os, sys

from bank import Bank, Client
from time import sleep

def display_title_bar():
    print('********************************************')
    print('       ~ Gringotts Wizarding Bank ~         ')
    print('********************************************')
    print()

 # Bank instance
bank1 = Bank('Gringottz Wizarding Bank')
# User instances for testing purpose
bank1.create_client('har_potter', 'Harry Potter') 
bank1.create_client('her_granger', 'Hermoine Granger')
bank1.create_client('alb_dumble', 'Albus Dumbledore')

#bank1.clients['har_potter'].deposit(200)

menu1 = ['[1] Create Account',
         '[2] Sign in',
         '[3] Client Database']

menu2 = ['[1] Check Balance', 
         '[2] Deposit Money',
         '[3] Withdraw Money',
         '[4] Exit']


def clear():
    '''Clear's the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    '''Function that starts the app'''

    clear()
    display_title_bar()
    for option in menu1:
        print(option)
    print()
    choice = int(input('> '))

    if choice == 1:
        create_customer_account()
    elif choice == 2:
        login()
    elif choice == 3:
        clear()
        display_title_bar()
        print('~ Client Database ~\n')
        print('Total customers: {}\n'.format(Client.total_clients))
        bank1.display_clients()
        
        x = input('\nEnter "Q" to go back: ')
        if x.lower() == 'q':
            main()

def create_customer_account():
    '''Create a customer/client instance with a username and fullname'''

    clear()
    display_title_bar()

    print('~ Create your bank account at {} ~\n'.format(bank1.name))
    username = input('Username: ')

    if ' ' in username: # Checks if username contains spaces
        print('Cannot contain spaces, please try again.')
        sleep(3)
        create_customer_account()
    fullname = input('Fullname: ')
    bank1.create_client(username, fullname)
    
    clear()
    display_title_bar()
    
    print('\n~ Account succesfull created! ~\n')
    print('Your username: {}'.format(username))
    print('Your fullname: {}\n'.format(fullname))
    print('Do you want to login? (Y/n)\n')
    answer = input('> ')

    if answer.lower() == 'n':
        main()
    else:
        login()

def login():
    '''Function that does a simple authentication'''
    clear()
    display_title_bar()
    
    print('~ Sign in ~\n')
    global auth # set auth to global so it can be used outside this function
    auth = input('Username: ')

    if auth.lower() in bank1.clients:
        # Show menu if username exist
        show_menu()
    else:
        print('Username is unknown. Try again')
        sleep(2)
        login()

def show_menu():
    '''
    Function that shows the menu and let the user interact with
    the BaseAccount class methods
    '''
    
    clear()
    display_title_bar()
    # Message to welcome user and show the logged in user
    print('~ Welcome {} ~\n'.format(bank1.clients[auth].display_name()))

    for option in menu2:
        print('{}'.format(option))
    print()
    choice = int(input('> '))

    if choice == 1:
        clear() 
        display_title_bar()
        # call and print get balance function
        print(bank1.clients[auth].get_balance()) # Show current balance

        print('\nEnter "Q" to go back: \n')
        done = input('> ')
        
        if done.lower() == 'q':
            show_menu()

    elif choice == 2:
        # call deposit function
        clear()
        display_title_bar()
        print(bank1.clients[auth].get_balance()) # Show current balance
        # Ask user to enter amount to deposit
        print('\nEnter amount to deposit: \n')
        
        amount = float(input('> '))
        bank1.clients[auth].deposit(amount)
        
        show_menu()

    elif choice == 3:
        # call withdraw function
        clear()
        display_title_bar()
        print(bank1.clients[auth].get_balance()) # Show current balance
        # Ask user to input amount to withdraw
        print('\nEnter amount to withdraw: \n')
        amount = float(input('> '))
        bank1.clients[auth].withdraw(amount)

        show_menu()

    elif choice == 4:
        clear()
        print('Goodbye ...')
        sleep(2)
        clear()
        sys.exit()

while True:
    main()
