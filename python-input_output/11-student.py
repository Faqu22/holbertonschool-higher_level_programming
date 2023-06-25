#!/usr/bin/python3
"""Task 8"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            filt = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filt[attr] = getattr(self, attr)
            return filt

    def reload_from_json(self, json):
        for element in json:
            if hasattr(self, element):
                setattr(self, element, json[element])
