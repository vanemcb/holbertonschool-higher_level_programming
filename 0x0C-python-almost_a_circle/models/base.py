#!/usr/bin/python3
""" Module class Base """
import json


class Base:
    """ Class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)
