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

    new_matrix = []

    if len(matrix) > 1:
        len_row = len(matrix[0])

    for row in range(len(matrix)):
        if len(matrix[row]) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
            break
        len_row = len(matrix[row])

        new_matrix.append([])
        for num in matrix[row]:
            if type(num) != int and type(num) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
                break


            new_matrix[row].append(round(num / div, 2))

    return new_matrix
