#!/usr/bin/python3
"""
    Function matrix_divided module
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats.
        div: number to divide each element of the matrix

    Returns:
        A new matrix divided.

    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []

    if type(matrix) != list:
        raise TypeError(error1)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == [] or matrix == [[]]:
        raise TypeError(error1)

    if len(matrix) > 1:
        len_row = len(matrix[0])

    for row in range(len(matrix)):
        if type(matrix[row]) != list:
            raise TypeError(error1)
        if len(matrix[row]) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
            break
        len_row = len(matrix[row])

        new_matrix.append([])
        for num in matrix[row]:
            if type(num) != int and type(num) != float:
                raise TypeError(error1)
                break

            new_matrix[row].append(round(num / div, 2))

    return new_matrix
