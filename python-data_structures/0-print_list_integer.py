#!/usr/bin/python3
def print_list_integer(my_list=[]):
    str = "{}"
    for x in range(0, len(my_list)):
        print(str.format(my_list[x]))
