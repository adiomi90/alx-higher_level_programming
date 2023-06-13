#!/usr/bin/python3
"""This class returns the dictionary description"""


def class_to_json(data):
    """obj is an instance of a Class"""
    return data.__dict__
