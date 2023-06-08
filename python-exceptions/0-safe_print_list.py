#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for y in my_list:
        print(y, end="")
        i += 1
        if x <= i:
            break
    print()
    return i
