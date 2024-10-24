from colorama import Fore
from infrastructure.switchlang import switch
import infrastructure.state as state

def run():
    print(' ****************** Welcome to Bhramonik **************** ')
    print()
    show_commands()
    while True:
        action = get_action()
        with switch(action) as s:
            s.case('c', create_account)
            s.case('a', log_into_account)
            s.case('l', list_listings)
            s.case('r', register_listing)
            s.case('u', update_availability)
            s.case('v', view_bookings)
            s.case('m', lambda: 'change_mode')
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)
        if action:
            print()
        if s.result == 'change_mode':
            return

def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('Login to your [a]ccount')
    print('[L]ist your listings')
    print('[R]egister a listing')
    print('[U]pdate listing availability')
    print('[V]iew your bookings')
    print('Change [M]ode (guest or host)')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

def create_account():
    print(' ****************** REGISTER **************** ')
    # TODO: Get name & email
    # TODO: Create account, set as logged in.
    print(" -------- NOT IMPLEMENTED -------- ")

def log_into_account():
    print(' ****************** LOGIN **************** ')
    # TODO: Get email
    # TODO: Find account in DB, set as logged in.
    print(" -------- NOT IMPLEMENTED -------- ")

def register_listing():
    print(' ****************** REGISTER LISTING **************** ')
    # TODO: Require an account
    # TODO: Get info about listing
    # TODO: Save listing to DB.
    print(" -------- NOT IMPLEMENTED -------- ")

def list_listings(supress_header=False):
    if not supress_header:
        print(' ******************     Your Listings     **************** ')
    # TODO: Require an account
    # TODO: Get listings, list details
    print(" -------- NOT IMPLEMENTED -------- ")

def update_availability():
    print(' ****************** Add available date **************** ')
    # TODO: Require an account
    # TODO: list listings
    # TODO: Choose listing
    # TODO: Set dates, save to DB.
    print(" -------- NOT IMPLEMENTED -------- ")

def view_bookings():
    print(' ****************** Your bookings **************** ')
    # TODO: Require an account
    # TODO: Get listings, and nested bookings as flat list
    # TODO: Print details for each
    print(" -------- NOT IMPLEMENTED -------- ")

def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()

def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '
    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()

def unknown_command():
    print("Sorry we didn't understand that command.")

def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)

def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)

if __name__ == '__main__':
    run()
