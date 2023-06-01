#!/usr/bin/python3
if __name__ == "__main__":
    for x in dir("hidden_4.pyc"):
        if x.startswith("__") is False:
            print(x)
