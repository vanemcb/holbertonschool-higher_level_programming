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

        list_attr = ["id", "size", "x", "y"]

        if len(args) != 0:
            for index, arg in enumerate(args):
                setattr(self, list_attr[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        my_dict = {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return my_dict
