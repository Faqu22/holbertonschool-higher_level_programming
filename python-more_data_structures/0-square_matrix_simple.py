#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = list(matrix)
    for y in range(len(matrix)):
        result[y] = list(map(lambda x: x ** 2, result[y]))
    return result
