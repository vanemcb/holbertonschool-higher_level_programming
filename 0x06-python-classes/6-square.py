#!/usr/bin/python3
"""
Class that defines a square.
"""


class Square:
    """Class that defines a square and prints a square"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        for n in position:
            if not isinstance(n, int) or n < 0 or len(position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            else:
                self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0 or self.__position[1] > 0:
            print()
        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        for n in self.__position:
            if not isinstance(n, int) or n < 0 or len(self.__position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            else:
                self.__position = value
