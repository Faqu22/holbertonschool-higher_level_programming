#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for x in range(0, list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            result.append(res)
    return result
