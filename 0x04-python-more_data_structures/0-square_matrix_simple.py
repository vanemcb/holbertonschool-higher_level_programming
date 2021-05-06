#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = [[x**2 for x in i] for i in matrix]
#    for i in matrix:
#        for x in i:
#            x = x**2
#            print(x)
    return matrix_square
