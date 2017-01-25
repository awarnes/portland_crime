"""
This module will retrieve files from civicapps.org for use in the Portland, Oregon Crime Analyzer.

Will save data to .../portland_crime/data_sets as .csv files.
Will also need to rename files with the correct year for the information it contains.
"""


import requests, os, csv
from bs4 import BeautifulSoup


# TODO: Make a set of retrieval functions to find, download, and unzip the .csv files from
#       civicapps.org


# def get_data_from_net(link_name, page_name=""):
#     """
#     Request information from CivicApps.org and format them for statistical processing.
#     """
#
#
#     response = requests.get(page_name + link_name)
#
#     all_crime_data = csv.DictReader(response.text)
#
#     return all_crime_data
