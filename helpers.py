"""
Helper function for sorted and groupby functions for organizing data.

***AT THIS POINT THIS IS NOT BEING USED BY PROGRAM***
"""


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




