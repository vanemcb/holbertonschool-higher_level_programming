#!/usr/bin/python3
""" Module to create Rectangle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Function to initialize an object"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Function that computes the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
