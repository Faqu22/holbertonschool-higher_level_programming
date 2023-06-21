#!/usr/bin/python3
"""1-my_list Module"""


class MyList(list):
    """class of an List"""

    def __init__(self):
        self = []

    def print_sorted(self):
        """print the list in the ascending sort"""
        i = sorted(self)
        for x in range(len(i)):
            print("{}{:d}{}".format("[" if x == 0 else " ", i[x],
                                    "," if x < len(i) - 1 else "]"), end="")
        print()
