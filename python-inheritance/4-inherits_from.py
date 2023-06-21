#!/usr/bin/python3
""" 4-inherits_from.py Module"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an instance \
    of a class that inherited (directly or indirectly) from the \
        specified class ; otherwise False."""
    return isinstance(obj, a_class)
