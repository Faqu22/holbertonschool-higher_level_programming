#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    x = ""
    i = 0
    for y in a_dictionary:
        if a_dictionary[y] > i:
            i = a_dictionary[y]
            x = y
    return x
