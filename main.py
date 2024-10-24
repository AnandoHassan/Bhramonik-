from colorama import Fore
import program_guests
import program_hosts

def main():
    # TODO: Setup mongoengine global values
    print_header()
    try:
        while True:
            if find_user_intent() == 'book':
                program_guests.run()
            else:
                program_hosts.run()
    except KeyboardInterrupt:
        return

def print_header():
    logo = \
        """ 
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
                      
-Let's book your stay for your next travel                            
                            """
    print(Fore.WHITE + '****************  BHRAMONIK  ****************')
    print(Fore.GREEN + logo)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Bhramonik!")
    print("Why are you here?")
    print()

def find_user_intent():
    print("[g] Book a place for your stay")
    print("[h] List your place for travelers")
    print()
    choice = input("Are you a [g]uest or [h]ost? ")
    if choice == 'h':
        return 'offer'
    return 'book'

if __name__ == '__main__':
    main()
