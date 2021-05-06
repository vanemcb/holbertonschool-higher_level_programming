#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[num[i]**2 for num in matrix] for i in range(len(matrix))]
    return matrix_square
