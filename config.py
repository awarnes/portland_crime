"""
Config file to import the DATA global variable.
"""

import main
from csv import reader
from os import (listdir, getcwd)
from collections import namedtuple

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
    print('Please enter the numbers associated with each file you want to use separated by a SPACE.')
    file_choices = input(">>> ").split()

    for choice in file_choices:
        datasets_chosen.append(dataset_options[int(choice)])

    return datasets_chosen


def open_dataset():
    """
    Opens data into the global scope DATA variable.
    :return:
    """
    global DATA

    dataset_names = choose_datasets()
    DATA = build_dataset(dataset_names)

    main.main_menu()
