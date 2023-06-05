#!/usr/bin/python3
"""
This module contains the function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not isinstance(matrix[0], list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return new_matrix
