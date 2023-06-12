#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def inherits_from(object_test, a_class):
    """Checks if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class
    """
    return issubclass(type(object_test), a_class) and type(object_test) is not a_class)
