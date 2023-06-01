#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    res = 0
    for x in argv:
        if count != 0:
            res = res + int(x)
        count += 1
    print("{}".format(res))
