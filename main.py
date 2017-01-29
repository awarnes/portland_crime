"""
This is the interface for the Portland, Oregon Crime Analyzer (POCA).

Questions:
    -Would it be better/possible to make one 'help' function and change the message?
    -Would it be better/possible to make one 'menu' function and change the options?
"""


#  General system imports
from os import (system, getcwd, listdir, chdir)
from csv import reader
from collections import namedtuple

#  Specific POCA module imports
from calculations import (calc_by_date, calc_by_time, calc_by_offense,
                          calc_by_address, calc_by_neighborhood, calc_by_precinct)
from control_flow import (pause_clear, leave, credits, main_menu_help, calc_menu_help)


def build_dataset(filenames):
    """
    Imports and formats data for calculations from any number of given files if they are in the correct location.
    """

    crime_data = dict()


    for name in filenames:
        crimes = list()
        with open(getcwd() + '/' + name, 'r') as csvreader:
            read_data = reader(csvreader)
            headings = ', '.join(next(read_data)).replace(' ', '')
            Data = namedtuple('Data', headings)

            for incident in read_data:
                crime = Data(*incident)
                crimes.append(crime)

            crime_data.update({name[20:24]: crimes})

    return crime_data


def choose_datasets():
    """
    Presents a menu option system for available datasets and returns a list of strings of them.
    """

    datasets_chosen = list()

    dataset_options = {index+1: filename for index, filename in enumerate(listdir()) if filename[-4:] == '.csv'}

    print("Which files do you want to use?")

    for datafile_key, datafile_value in sorted(dataset_options.items()):
        print("{}: {}".format(datafile_key, datafile_value))
    print()
    print('Please enter the numbers associated with each file you want to use separated by a space')
    file_choices = input(">>> ").split()

    for choice in file_choices:
        datasets_chosen.append(dataset_options[int(choice)])

    return datasets_chosen


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
        pause_clear()
        calc_overview_menu()


def main_menu():
    """
    Displays the main menu of the program for user interaction.
    """

    main_menu_options = {1: 'Calculations.', 2: 'Update your Database!',
                         3: 'Help', 4: 'Credits', 5: 'Quit'}

    main_menu_functions = {1: calc_overview_menu, 2: '',
                         3: main_menu_help, 4: credits, 5: leave}

    for mmenu_key, mmenu_value in main_menu_options.items():
        print("{}: {}".format(mmenu_key, mmenu_value))

    try:
        main_menu_choice = int(input("Which one do you want?" ))
        os.system('clear')
        main_menu_functions[main_menu_choice]()
    except (ValueError, KeyError):
        print("Invalid choice. Please enter the number of the option you want.")
        pause_clear()
        main_menu()


if __name__ == '__main__':

    # Ensure that the program is pointed to the right place in order to read files.
    basepath = '/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/'

    system('clear')
    print("Do you need to change the base filepath for your .csv files?")
    filepath_yn = input("Y/N: ")

    if 'y' in filepath_yn.lower():
        print('Please enter the absolute filepath to your data directory.')
        basepath = input('>>> ')

    if getcwd() != basepath:
        chdir(basepath)

    system('clear')
    print("Welcome to the Portland, Oregon Crime Analyzer (POCA)")
    pause_clear()

    main_menu_help()