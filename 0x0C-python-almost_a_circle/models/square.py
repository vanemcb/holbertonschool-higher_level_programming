#!/usr/bin/python3
""" Module class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return "[Square]({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):

        if len(args) != 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                if index == 1:
                    self.width = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        my_dict = {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return my_dict
