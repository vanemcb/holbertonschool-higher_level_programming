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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = type(list_objs[0]).__name__ + ".json"
        list_dict = []
        with open(filename, "w", encoding="utf-8") as file:
            for dicts in list_objs:
                list_dict.append(cls.to_dictionary(dicts))
            file.write(json.dumps(list_dict))
