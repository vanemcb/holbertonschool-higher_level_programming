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
