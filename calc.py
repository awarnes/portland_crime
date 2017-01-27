"""POCA: CALC
    The module with the functions to perform calculations on data sets in .../portland_crime/data_sets

    These will be imported to main.py in order to provide feedback to the user.
"""

import os
from collections import (namedtuple, Counter, defaultdict)
from csv import reader





def build_dataset(filenames, base_path="/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/"):
    """
    Imports and formats data for calculations from any number of given files if they are in the correct location.
    """

    crime_data = dict()


    for name in filenames:
        crimes = list()
        with open(base_path + name, 'r') as csvreader:
            read_data = reader(csvreader)
            headings = ', '.join(next(read_data)).replace(' ', '')
            Data = namedtuple('Data', headings)

            for incident in read_data:
                crime = Data(*incident)
                crimes.append(crime)

            crime_data.update({name[20:24]: crimes})

    return crime_data


def choose_datasets(base_path="/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/"):
    """
    Presents a menu option system for available datasets and returns a list of strings of them.
    """

    datasets_chosen = list()

    if os.getcwd() != "/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/":
        os.chdir("/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/")

    print()
    print("Do you need to change the base filepath for your .csv files?")
    filepath_yn = input("Y/N: ")


    if 'y' in filepath_yn:
        print("Where are your .csv data sets stored? (Please enter full filepath)")
        base_path = input(">>> ")

    dataset_options = {index+1: filename for index, filename in enumerate(os.listdir()) if filename[-4:] == '.csv'}

    print("Which files do you want to use?")

    for datafile_key, datafile_value in sorted(dataset_options.items()):
        print("{}: {}".format(datafile_key, datafile_value))
    print()
    print('Please enter the numbers associated with each file you want to use separated by a space')
    file_choices = input(">>> ").split()

    for choice in file_choices:
        datasets_chosen.append(dataset_options[int(choice)])

    return datasets_chosen


def sort_by_offense_helper(incident):
    """
    Helper function for sorted() and groupby() to sort by MajorOffenseType, index=3
    """


    offense = incident.MajorOffenseType
    return offense


def sort_by_date_helper(incident):
    """
    Helper function for sorted() and groupby() to sort by ReportDate, index=1
    """


    date = incident.ReportDate
    return date


def sort_by_time_helper(incident):
    """
    Helper function for sorted() and groupby() to sort by ReportTime, index=2
    """


    time = incident.ReportTime
    return time


def sort_by_neighborhood_helper(incident):
    """
    Helper function for sorted() and groupby() to sort by Neighborhood, index=5
    """


    neighborhood = incident.Neighborhood
    return neighborhood


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

    input("...")
    os.system("clear")


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

    input("...")
    os.system("clear")


def data_average():
    """
    Returns the max() of the search terms.
    """


    print("WORK IN PROGRESS!!!")
    input("...")
    os.system("clear")

def calc_by_date():
    """
    Menu to calculate certain information oriented by date.
    """


    dataset_names = choose_datasets()
    data = build_dataset(dataset_names)

    # for dataset_key in data.keys():
    #     data = sorted(data[dataset_key], key=sort_by_offense_helper)

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](data, 'ReportDate')


def calc_by_time():
    """
    Menu to calculate certain information oriented by time of day.
    """


    dataset_names = choose_datasets()
    data = build_dataset(dataset_names)

    # for dataset_key in data.keys():
    #     data = sorted(data[dataset_key], key=sort_by_offense_helper)

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](data, 'ReportTime')


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


def calc_by_offense():
    """
    Menu to calculate certain information oriented by offense type.
    """


    dataset_names = choose_datasets()
    data = build_dataset(dataset_names)

    # for dataset_key in data.keys():
    #     data = sorted(data[dataset_key], key=sort_by_offense_helper)

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](data, 'MajorOffenseType')



def calc_by_address():
    """
    Menu to calculate certain information oriented by address.
    """


    dataset_names = choose_datasets()
    data = build_dataset(dataset_names)

    # for dataset_key in data.keys():
    #     data = sorted(data[dataset_key], key=sort_by_offense_helper)

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](data, 'Address')


def calc_by_neighborhood():
    """
    Menu to calculate certain information oriented by neighborhood.
    """


    dataset_names = choose_datasets()
    data = build_dataset(dataset_names)

    # for dataset_key in data.keys():
    #     data = sorted(data[dataset_key], key=sort_by_offense_helper)

    calc_functions = {1: data_min, 2: data_max, 3: data_average}

    calc_choice = calc_options_menu()

    calc_functions[calc_choice](data, 'Neighborhood')


def calc_by_precinct():
    """
    Menu to calculate certain information oriented by police precinct and district.
    """


    pass



# TODO: Make functions to perform calculations on data.
