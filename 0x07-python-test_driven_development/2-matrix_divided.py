#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide the elements of a given matrix by div,
    rounding to 2 decimal places.

    Args:
        matrix (list of list): A given matrix.
        div (int or float): A given number.

    Returns:
        list of list: A new matrix with rounded results.
    """
    if (
        matrix == []
        or not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        new_row = []
        for element in row:
            new_value = round(element / div, 2)
            new_row.append(new_value)
        result_matrix.append(new_row)

    return result_matrix
