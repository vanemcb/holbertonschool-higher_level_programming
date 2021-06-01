#!/usr/bin/python3
""" Module to create MyList class """

class MyList(list):
    """ class that inherits from list """

    def print_sorted(self):
        print(sorted(self))
