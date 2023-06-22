#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """ Function that write at the end of a text file (UTF8) and prints it"""
    with open(filename, "a+", encoding="utf-8") as x:
        x.write(text)
    return len(text)
