#!/usr/bin/python3
"""Module to write an object to a text file"""
import json


def save_to_json_file(data, filename):
    """Function that writes an Object to file"""

    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(data, f)
