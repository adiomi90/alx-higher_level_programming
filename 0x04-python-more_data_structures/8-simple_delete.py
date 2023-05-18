#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for x in a_dictionary:
        if x == key:
            dictionary[x].pop()
    return a_dictionary
