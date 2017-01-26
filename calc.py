"""POCA: CALC
    The module with the functions to perform calculations on data sets in .../portland_crime/data_sets

    These will be imported to main.py in order to provide feedback to the user.
"""


def get_data(num_files, *filenames, base_path="/portland_crime/data_sets/"):
    """
    Imports and formats data for calculations from any number of files.
    """


    data = list()

    for _ in range(num_files):
        with open(base_path+filenames[_], 'r') as csvreader:
            reader = csv.D

    return data


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
