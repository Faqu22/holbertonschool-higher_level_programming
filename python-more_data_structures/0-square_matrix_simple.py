#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(matrix)
    y, x = 0, 0
    for y in range(0, len(new_matrix)):
        for x in range(0, len(new_matrix[y])):
            new_matrix[y][x] = matrix[y][x] ** 2
    return new_matrix
