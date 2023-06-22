#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """ Function that reads a text file (UTF8) and prints it"""
    with open(filename, "r") as x:
        for i in x.readlines():
            print("{}".format(i), end="")
