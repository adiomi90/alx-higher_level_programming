#!/usr/bin/python3
"""Module that returns an object represented by JSON"""
import json


def from_json_string(input_json):
    """Function return a json to object"""

    return json.loads(input_json)
