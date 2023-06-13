#!/usr/bin/python3
"""Module to create an Object"""
import json


def load_from_json_file(filename):
    """Function creates an Object from a JSON file"""

    with open(filename, encoding='utf-8') as output:
        return json.load(output)
