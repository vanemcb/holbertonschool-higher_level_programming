#!/usr/bin/python3
""" Class that defines a rectangle. """


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """ Object Ractangle initialization """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Instance method to get the attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Instance method to set the attribute width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Instance method to get the attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Instance method to set the attribute height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Instance method to compute the area rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Instance method to compute the perimeter rectangle """
        if self.__width == 0 or self.__height == 0:
            peri = 0
        else:
            peri = (self.__height * 2) + (self.__width * 2)
        return peri

    def __str__(self):
        """ Instance method to print the rectangle with the character """
        if self.__width == 0 or self.__height == 0:
            display_rectangle = ""
        else:
            display = []
            for row in range(self.__height):
                row_display = ""
                for column in range(self.__width):
                    row_display += "#"
                display.append(row_display)
            display_rectangle = "\n".join(display)
        return display_rectangle

    def __repr__(self):
        """ Instance method to return a string
        representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Instance method to print a message when
        an object is deleted """
        print("Bye rectangle...")
