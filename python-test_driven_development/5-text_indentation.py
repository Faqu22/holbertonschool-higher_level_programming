#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = ''
    for i in text:
        if x != '.' and x != '?' and x != ':':
            print(i, end="")
        else:
            print("\n")
        x = i
