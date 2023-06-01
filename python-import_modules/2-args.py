#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    if len(argv) < 2:
        print("0 arguments.")
    else:
        print("{} {}".format(len(argv) - 1,
                             "arguments:" if len(argv) > 2 else "argument:"))
        for x in argv:
            if count != 0:
                print("{}: {}".format(count, x))
            count += 1
