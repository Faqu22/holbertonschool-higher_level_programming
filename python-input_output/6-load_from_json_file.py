#!/usr/bin/python3
"""Task 6"""
import json


def load_from_json_file(filename):
    """Function that returns an object (Python data structure)\
        represented by a JSON string"""
    with open(filename) as x:
        data_obj = json.load(x)
    return data_obj
