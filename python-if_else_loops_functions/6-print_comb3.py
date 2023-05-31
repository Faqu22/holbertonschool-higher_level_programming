#!/usr/bin/python3

for y in range(0, 9):
    for x in range(y + 1, 10):
        print("{}{}{}".format(y, x,
                              (", " if x < 10 and y < 8 else "\n")), end='')
