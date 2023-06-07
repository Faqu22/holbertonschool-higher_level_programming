#!/usr/bin/python3
def whatRoman(i):
    if i == 'I':
        return 1
    elif i == 'V':
        return 5
    elif i == 'X':
        return 10
    elif i == 'L':
        return 50
    elif i == 'C':
        return 100
    elif i == 'D':
        return 500
    elif i == 'M':
        return 1000
    else:
        return 0


def roman_to_int(roman_string):
    result = list(map(whatRoman, roman_string))
    x, y = '', 0
    letterI = {'I': 0, 'V': -2, 'X': -2, 'L': -2, 'C': -2, 'D': -2, 'M': -2}
    letterX = {'I': 0, 'V': 0, 'X': 0, 'L': -20, 'C': -20, 'D': -20, 'M': -20}
    letterC = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': -200, 'M': -200}

    for let in roman_string:
        if x == 'I':
            y += letterI[let]
        elif x == 'X':
            y += letterX[let]
        elif x == 'C':
            y += letterC[let]
        x = let

    for x in result:
        if x == 0:
            return 0
        y += x
    return y
