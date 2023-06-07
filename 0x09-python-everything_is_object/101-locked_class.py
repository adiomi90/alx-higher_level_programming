#!/usr/bin/python3
"""
   Defines class with no class or object attribute
   Control dynamically created instance attribute
"""


class LockedClass:
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = ["first_name"]
