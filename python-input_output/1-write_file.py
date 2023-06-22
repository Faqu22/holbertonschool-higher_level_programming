#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """ Function that write a text file (UTF8) and prints it"""
    with open(filename, "w", encoding="utf-8") as x:
        x.write(text)
    return len(text)
