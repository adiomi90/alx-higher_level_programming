#!/usr/bin/python3

def find_peak(list_of_integers):
    """ Args:
           list_of_integer(list): Unsorted list
        Returns:
            int: The peak of the unsorted list
    """

    length = len(list_of_integers)

    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]

    peak = list_of_integers[0]

    for i in range(1, length):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]

    return peak
