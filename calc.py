"""POCA: CALC
    The module with the functions to perform calculations on data sets in .../portland_crime/data_sets

    These will be imported to main.py in order to provide feedback to the user.
"""

from control_flow import pause_clear
import config
from collections import (Counter, defaultdict)


def data_max(data, check_type):
    """
    Returns the max() of the search terms.
    """

    offense_dict = defaultdict(list)

    for eachkey in data:
        for incident in data[eachkey]:
            offense_dict[eachkey].append(getattr(incident, check_type))

        c = Counter(offense_dict[eachkey])
        print("The most common {} in {} was {} with {} incidents.".format(check_type, eachkey, c.most_common()[0][0], c.most_common()[0][1]))

    pause_clear()


def data_min(data, check_type):
    """
    Returns the max() of the search terms.
    """

    # return_dict = {'ReportDate': calc_by_date, 'ReportTime': calc_by_time, 'MajorOffenseType': calc_by_offense, 'Address': calc_by_address, 'Neighborhood': calc_by_neighborhood} # Make something to return to the previous menu when done with data based off of check_type

    offense_dict = defaultdict(list)

    for eachkey in data:
        for incident in data[eachkey]:
            offense_dict[eachkey].append(getattr(incident, check_type))

        c = Counter(offense_dict[eachkey])
        print("The least common {} in {} was {} with {} incidents.".format(check_type, eachkey, c.most_common()[-1][0], c.most_common()[-1][1]))

    pause_clear()


def data_average(data, check_type):
    """
    Returns the max() of the search terms.
    """


    print("WORK IN PROGRESS!!!")
    pause_clear()


def by_date():
    """
    Menu to calculate certain information oriented by date.
    """

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](config.DATA, 'ReportDate')


def by_time():
    """
    Menu to calculate certain information oriented by time of day.
    """

    # for dataset_key in data.keys():
    #     data = sorted(data[dataset_key], key=sort_by_offense_helper)

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](config.DATA, 'ReportTime')


def by_offense():
    """
    Menu to calculate certain information oriented by offense type.
    """

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](config.DATA, 'MajorOffenseType')


def by_address():
    """
    Menu to calculate certain information oriented by address.
    """

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](config.DATA, 'Address')


def by_neighborhood():
    """
    Menu to calculate certain information oriented by neighborhood.
    """

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](config.DATA, 'Neighborhood')


def by_precinct():
    """
    Menu to calculate certain information oriented by police precinct and district.
    """

    pass


def calc_options_menu():
    """
    Prints a menu for a variety of calculation options and returns the choice of the option.
    """


    calc_options = {1: 'Min', 2: 'Max', 3: 'Average'}
    print()
    for copt_key, copt_value in calc_options.items():
        print("{}: {}".format(copt_key, copt_value))

    print("Which one do you want?")
    try:
        copt_choice = int(input(">>> "))
        if copt_choice in calc_options.keys():
            return copt_choice
        else:
            print("Invalid choice. Please enter the number next to the selection you want.")
            calc_options_menu()
            return int(copt_choice)
    except ValueError:
        print("Invalid choice. Please enter the number next to the selection you want.")
        calc_options_menu()
    finally:
        return int(copt_choice)


# TODO: Make functions to perform calculations on data.
