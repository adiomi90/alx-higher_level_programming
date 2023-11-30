#!/usr/bin/python3
"""DEfines a function that finds the peak in a list of unsroted numbers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integer(list): Unsorted list
    Returns:
        int: The peak of the unsorted list
    """

    length = len(list_of_integers)

    if not list_of_integers:
        return None

    if length == 1:
        return list_of_integers[0]

    if length == 2:
        return max(list_of_integers)
    
    list_of_integers.sort(reverse=True)

    return list_of_integers[0]
