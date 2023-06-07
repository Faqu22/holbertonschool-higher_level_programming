#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1, s2 = list(set(set_1)), list(set(set_2))
    comm = list(set(s1).symmetric_difference(set(s2)))
    return comm
