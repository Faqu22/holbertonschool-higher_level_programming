#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for x in range(len(my_list)):
        new_list[x] = (False if my_list[x] % 2 != 0 else True)
    return new_list
