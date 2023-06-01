#!/usr/bin/python3
from sys import argv
count = 0
if len(argv) < 2:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(argv)))
    for x in argv:
        if count != 0:
            print("{}: {}".format(count, x))
        count = count + 1
