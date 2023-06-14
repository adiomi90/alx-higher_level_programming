#!/usr/bin/python3
"""
Module for the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to the end of a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        new_lines = []
        for i in range(len(lines)):
            new_lines.append(lines[i])
            if search_string in lines[i]:
                new_lines.append(new_string)
        f.writelines(new_lines)
