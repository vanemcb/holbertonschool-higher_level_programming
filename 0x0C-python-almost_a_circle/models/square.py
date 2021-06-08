#!/usr/bin/python3
""" Module class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ Method that return the following format string:
        [Square] (<id>) <x>/<y> - <size> """

        return "[Square]({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Method that assigns a key/value argument to attributes """

        list_attr = ["id", "size", "x", "y"]

        if len(args) != 0:
            for index, arg in enumerate(args):
                setattr(self, list_attr[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method that returns the dictionary representation
        of a Square """
        my_dict = {
            "id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return my_dict
