#!/usr/bin/python3
from sys import argv
count = 0
print("{}{}".format(len(argv) - 1,
                    " arguments:" if len(argv) > 1 else " arguments."))
for x in argv:
    if count != 0:
        print("{}: {}".format(count, x))
    count = count + 1
