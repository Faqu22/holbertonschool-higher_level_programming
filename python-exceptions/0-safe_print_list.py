#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if x == 0:
        print(my_list[x], end="")
    for y in range(0, x):
        try:
            print(my_list[y], end="")
            i += 1
        except:
            break
    print()
    return i
