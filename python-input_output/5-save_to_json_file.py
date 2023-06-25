#!/usr/bin/python3
"""Task 5"""


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file, using a JSON\
        Representation"""
    with open(filename, "w", encoding="utf-8") as x:
        x.write(str(my_obj))
