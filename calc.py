"""POCA: CALC
    The module with the functions to perform calculations on data sets in .../portland_crime/data_sets

    These will be imported to main.py in order to provide feedback to the user.
"""


from collections import namedtuple
from csv import reader


def build_dataset(*filenames, base_path="/Users/alexanderwarnes/Documents/abw_codes/Git/projects/portland_crime/data_sets/"):
    """
    Imports and formats data for calculations from any number of files.
    """

    crime_data = dict()


    for name in filenames:
        crimes = list()
        with open(base_path + name, 'r') as csvreader:
            reader = csv.reader(csvreader)
            headings = ', '.join(next(reader)).replace(' ', )
            Data = namedtuple('Data', headings)

            for incident in reader:
                crime = Data(*incident)
                crimes.append(crime)

            crime_data.update({name[20:24]: crimes})

    return crime_data


def sort_by_crime_helper(incident):
    """
    Helper function for sorted() and groupby() to sort by MajorOffenseType, index=3
    """


    offense = incident[3]
    return offense


def sort_by_crime_helper(incident):
    """
    Helper function for sorted() and groupby() to sort by MajorOffenseType, index=3
    """


    offense = incident[3]
    return offense


def data_max():
    """
    Returns the max() of the search terms.
    """


    pass


def data_min():
    """
    Returns the max() of the search terms.
    """


    pass


def calc_by_date():
    """
    Menu to calculate certain information oriented by date.
    """


    pass


def calc_by_time():
    """
    Menu to calculate certain information oriented by time of day.
    """


    pass


def calc_by_offense():
    """
    Menu to calculate certain information oriented by offense type.
    """


    pass


def calc_by_address():
    """
    Menu to calculate certain information oriented by address.
    """


    pass


def calc_by_neighborhood():
    """
    Menu to calculate certain information oriented by neighborhood.
    """


    pass


def calc_by_precinct():
    """
    Menu to calculate certain information oriented by police precinct and district.
    """


    pass



# TODO: Make functions to perform calculations on data.
