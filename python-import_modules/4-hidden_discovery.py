#!/usr/bin/python
if __name__ == "__main__":
    text = dir("hidden_4.pyc")
    for x in text:
        if x[:2] != "__":
            print(x)
