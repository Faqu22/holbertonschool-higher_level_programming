#!/usr/bin/python3
def no_c(my_string):
    c_string = list(my_string)
    for x in range(0, len(c_string)):
        if c_string[x] == 'c' or c_string[x] == 'C':
            c_string[x] = ''
    c_string = ''.join(c_string)
    return c_string
