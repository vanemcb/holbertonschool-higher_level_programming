#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in range(0, len(i)):
            print("{:d}".format(i[x]), end=" ")
        print("")
