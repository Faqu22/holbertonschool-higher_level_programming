#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "":
        return
    try:
        a_dictionary.pop(key)
    except a_dictionary[key].DoesNotExist:
        pass
    return a_dictionary
