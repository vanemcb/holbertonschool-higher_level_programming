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
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string == None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_dict = []
        with open(filename, "w", encoding="utf-8") as file:
            for dicts in list_objs:
                list_dict.append(cls.to_dictionary(dicts))
            file.write(json.dumps(list_dict))

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(4, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        my_list = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                my_list = cls.from_json_string(file.read())
            for index in range(len(my_list)):
                my_list[index] = cls.create(**my_list[index])
        except:
            pass
        return my_list
