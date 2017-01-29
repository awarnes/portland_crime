"""
Helper functions for the POCA
"""


from os import system


def pause_clear():
    """
    Wait for user input, clear the screen, then continue.
    :return: None
    """

    input('...')
    system('clear')
    return None


def leave():
    """Quits program"""


    print("Are you sure you want to quit?")
    leave_yn = input("Y/N: ")

    if 'y' in leave_yn.lower():
        print("Thanks for stopping by!")
        print("Come back soon!")
        pause_clear()
        exit()

    elif 'n' in leave_yn.lower():
        pause_clear()
        main_menu()

    else:
        print("I'm not sure what you mean!")
        pause_clear()
        leave()


def credits():
    """
    General credits for the program.
    :return: None
    """

    system('clear')
    print("Credits:")
    print("--------")
    print("Coded by: Alexander Warnes")
    print()
    print("Data from: CivicApps.org")
    pause_clear()
    main_menu()


def calc_menu_help():
    """
    Displays the help file for the calc_menu.
    """

    os.system("clear")
    print("CALC MENU HELP!!!!!")
    pause_clear()
    calc_overview_menu() #  This help pane is only callable from the calc_menu


def main_menu_help():
    """
    Displays a general introduction and help message to the user.
    First called at initialization, then called again when asked for by user.
    """

    print("MAIN MENU HELP MESSAGE!")
    pause_clear()
    main_menu() #  This help function is only callable from the main menu.
