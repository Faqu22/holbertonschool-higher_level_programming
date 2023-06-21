#!/usr/bin/python3
"""1-my_list Module"""


class MyList(list):
    """class of an List"""

    def __init__(self):
        self = []

    def print_sorted(self):
        """print the list in the ascending sort"""
        x = sorted(self)
        print(x)
