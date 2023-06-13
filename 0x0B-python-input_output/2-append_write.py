#!/usr/bin/python3
"""Module that appends a string at the end of a txt file"""


def append_write(filename="", text=""):
    """Function appends a string at the end of a text"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
