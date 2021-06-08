#!/usr/bin/python3
""" Module class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def display(self):
        for z in range(self.y):
            print()
        for x in range(self.height):
            for y in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):

        list_attr = ["id", "width", "height", "x", "y"]

        if len(args) != 0:
            for index, arg in enumerate(args):
                setattr(self, list_attr[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        my_dict = {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                    }
        return my_dict

    @property
    def width(self):
        """ Getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
