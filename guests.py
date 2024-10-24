from infrastructure.switchlang import switch
import  hosts
import infrastructure.state as state

def run():
    print(' ****************** Welcome to Bhramonik **************** ')
    print()
    show_commands()
    try:
        while True:
            action = hosts.get_action()
            with switch(action) as s:
                s.case('c', hosts.create_account)
                s.case('l', hosts.log_into_account)
                s.case('a', add_a_listing)
                s.case('y', view_your_listings)
                s.case('b', book_a_stay)
                s.case('v', view_bookings)
                s.case('m', lambda: 'change_mode')
                s.case('?', show_commands)
                s.case('', lambda: None)
                s.case(['x', 'bye', 'exit', 'exit()'], hosts.exit_app)
                s.default(hosts.unknown_command)
            state.reload_account()
            if action:
                print()
            if s.result == 'change_mode':
                return
    except KeyboardInterrupt:
        return

def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('[L]ogin to your account')
    print('[B]ook a place')
    print('[A]dd a listing')
    print('View [Y]our listings')
    print('[V]iew your bookings')
    print('[M]ain menu')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

def add_a_listing():
    print(' ****************** Add a Listing **************** ')
    # TODO: Require an account
    # TODO: Get listing info from user
    # TODO: Create the listing in the DB.
    print(" -------- NOT IMPLEMENTED -------- ")

def view_your_listings():
    print(' ****************** Your Listings **************** ')
    # TODO: Require an account
    # TODO: Get listings from DB, show details list
    print(" -------- NOT IMPLEMENTED -------- ")

def book_a_stay():
    print(' ****************** Book a Stay **************** ')
    # TODO: Require an account
    # TODO: Verify they have a profile
    # TODO: Get dates and select listing
    # TODO: Find listings available across date range
    # TODO: Let user select listing to book.
    print(" -------- NOT IMPLEMENTED -------- ")

def view_bookings():
    print(' ****************** Your Bookings **************** ')
    # TODO: Require an account
    # TODO: List booking info along with listing info
    print(" -------- NOT IMPLEMENTED -------- ")

if __name__ == '__main__':
    main()
