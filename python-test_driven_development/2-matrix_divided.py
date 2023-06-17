#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(element, list) for element in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for x in i:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")        

    new = list(matrix)

    for i in range(len(matrix)):
        new[i] = list(map(lambda x: round(x / div, 2), new[i]))    
    return new
