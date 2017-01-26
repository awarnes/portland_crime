"""
This is the interface for the Portland, Oregon Crime Analyzer (POCA).

Questions:
    -Would it be better/possible to make one 'help' function and change the message?
    -Would it be better/possible to make one 'menu' function and change the options?
"""


#  General system imports
import os,

#  Specific calc module imports
from calc import (calc_by_date, calc_by_time, calc_by_offense,
                 calc_by_address, calc_by_neighborhood, calc_by_precinct)


def calc_general_menu_help():
    """
    Displays the help file for the calc_menu.
    """

    os.system("clear")
    print("CALC MENU HELP!!!!!")
    input("...") #  Wait for any user input
    os.system("clear")
    calc_overview_menu() #  This help pane is only callable from the calc_menu


def calc_overview_menu():
    """
    A menu for all the calculation methods of the calc module.
    Wants:
        -To allow the user to choose intuitively between comparing multiple years (files) and within one file.
        -To allow the user to choose any type of math operation that they want (function creator??)
        -To allow the user to save data from their calculations.
        -To allow the user to create nice looking graphs from their calculations.
        -To allow the user to export their calculations into various formats (....?)
    """


    calc_menu_options = {1: 'Calculate by Report Date', 2: 'Calculate by Report Time', 3: 'Calculate by Major Offense Type',
                         4: 'Calculate by Address', 5: 'Calculate by Neighborhood',
                         6: 'Calculate by Police Precinct and District', 7: 'Load a prior session.',
                         8: 'Help', 9: 'Back'}

    calc_menu_functions = {1: calc_by_date, 2: calc_by_time, 3: calc_by_offense,
                           4: calc_by_address, 5: calc_by_neighborhood, 6: calc_by_precinct,
                           7: None, 8: calc_menu_help, 9: main_menu}

    for cmenu_key, cmenu_value in calc_menu_options.items():
        print("{}: {}.".format(cmenu_key, cmenu_value))

    try:
        calc_menu_choice = int(input("Which one do you want? "))
        os.system('clear')
        calc_menu_functions[calc_menu_choice]()
    except (KeyError, ValueError):
        print("Invalid choice. Please enter the number of the option you want.")
        calc_overview_menu()


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


def main_help_message():
    """
    Displays a general introduction and help message to the user.
    First called at initialization, then called again when asked for by user.
    """


    print("MAIN MENU HELP MESSAGE!")
    input("...") #  To allow for user input before clearing the screen.
    os.system("clear")
    main_menu() #  This help function is only callable from the main menu.


def main_menu():
    """
    Displays the main menu of the program for user interaction.
    """

    main_menu_options = {1: 'Calculations!', 2: 'Update your Database!',
                         3: 'General Help', 4: 'Credits', 5: 'Quit'}

    main_menu_functions = {1: calc_menu, 2: update_menu,
                         3: main_help_message, 4: credits, 5: leave}

    for mmenu_key, mmenu_value in main_menu_options.items():
        print("{}: {}.".format(mmenu_key, mmenu_value))

    try:
        main_menu_choice = int(input("Which one do you want?" ))
        os.system('clear')
        main_menu_functions[main_menu_choice]()
    except (ValueError, KeyError):
        print("Invalid choice. Please enter the number of the option you want.")
        main_menu()


def initialize():
    """
    Initializes the program with a basic help and welcome message.
    """


    print("Welcome to the Portland, Oregon Crime Analyzer (POCA)")

    main_help_message()


initialize()
