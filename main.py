"""
This is the interface for the Portland, Oregon Crime Analyzer (POCA).

Questions:
    -Would it be better/possible to make one 'help' function and change the message?
    -Would it be better/possible to make one 'menu' function and change the options?
"""


#  General system imports
from os import (system, getcwd, chdir)

#  Specific POCA module imports
import calc
import control_flow
import config


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

    calc_menu_functions = {1: calc.by_date, 2: calc.by_time, 3: calc.by_offense,
                           4: calc.by_address, 5: calc.by_neighborhood, 6: calc.by_precinct,
                           7: None, 8: control_flow.calc_menu_help, 9: main_menu}

    for cmenu_key, cmenu_value in calc_menu_options.items():
        print("{}: {}.".format(cmenu_key, cmenu_value))

    try:
        calc_menu_choice = int(input("Which one do you want? "))
        system('clear')
        calc_menu_functions[calc_menu_choice]()
    except (KeyError, ValueError):
        print("Invalid choice. Please enter the number of the option you want.")
        control_flow.pause_clear()
        calc_overview_menu()


def main_menu():
    """
    Displays the main menu of the program for user interaction.
    """

    main_menu_options = {1: 'Perform calculations.', 2: 'Open new data sets.',
                         3: 'Help', 4: 'Credits', 5: 'Quit'}

    main_menu_functions = {1: calc_overview_menu, 2: config.open_new_dataset,
                           3: control_flow.main_menu_help, 4: control_flow.credits, 5: control_flow.leave}

    for mmenu_key, mmenu_value in main_menu_options.items():
        print("{}: {}".format(mmenu_key, mmenu_value))

    try:
        main_menu_choice = int(input("Which one do you want?" ))
        system('clear')
        main_menu_functions[main_menu_choice]()
    except (ValueError, KeyError):
        print("Invalid choice. Please enter the number of the option you want.")
        control_flow.pause_clear()
        main_menu()


if __name__ == '__main__':

    # Ensure that the program is pointed to the right place in order to read files.
    basepath = '/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/'

    system('clear')
    print("Do you need to change the base file path for your .csv files?")
    filepath_yn = input("Y/N: ")
    print(type(filepath_yn))

    if 'y' in filepath_yn.lower():
        print('Please enter the absolute file path to your data directory.')
        basepath = input('>>> ')

    if getcwd() != basepath:
        chdir(basepath)

    config.open_dataset()

    system('clear')
    print("Welcome to the Portland, Oregon Crime Analyzer (POCA)")
    control_flow.pause_clear()

    control_flow.main_menu_help()