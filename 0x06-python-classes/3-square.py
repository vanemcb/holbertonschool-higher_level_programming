#!/usr/bin/python3
"""
Class that defines a square.
"""


class Square:
    """ Class that defines a square and its area."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that computes the square area.

            Returns:
                The current square area.

        """
        return self.__size ** 2
