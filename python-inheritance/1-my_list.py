#!/usr/bin/python3
"""1-my_list Module"""


class MyList(list):
    """class of an List"""

    def print_sorted(self):
        """print the list in the ascending sort"""
        print(sorted(self))
