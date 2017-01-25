"""
This is the interface for the Portland, Oregon Crime Analyzer.
"""


def leave():
    """Quits program"""


    print("Are you sure you want to quit?")
    leave_yn = input("Y/N: ")

    if 'y' in leave_yn.lower():
        print("Thanks for stopping by!")
        print("Come back soon!")
        input("...")
        os.system("clear")
        exit()

    elif 'n' in leave_yn.lower():
        main_menu()

    else:
        print("I'm not sure what you mean!")
        leave()


def main_menu():
    pass


def initialize():
    pass


initialize()
