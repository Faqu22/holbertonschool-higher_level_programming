#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for x in range(0, list_length):
        try:
            result.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
    return result
