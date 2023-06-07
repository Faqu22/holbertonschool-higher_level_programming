#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except a_dictionary[key].DoesNotExist:
        print("Pero")
    return a_dictionary
