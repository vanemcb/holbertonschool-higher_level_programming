#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in matrix:
        for x in range(0, len(i)):
            if x < len(i) - 1:
                print("{:d}".format(i[x]), end=" ")
            else:
                print("{:d}".format(i[x]))
