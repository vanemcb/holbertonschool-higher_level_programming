#!/usr/bin/python3
"""
    Function print_square module
"""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size: square size.

    """

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
