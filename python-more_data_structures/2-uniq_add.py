#!/usr/bin/python3
def uniq_add(my_list=[]):
    res, uniq = 0, set(my_list)
    for x in uniq:
        res += x
    return res
