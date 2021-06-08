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
        """  Static method that returns the JSON string
        representation of list_dictionaries """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Static method that returns the list of the
        JSON string representation json_string """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method hat writes the JSON string
        representation of list_objs to a file """

        filename = cls.__name__ + ".json"
        list_dict = []
        with open(filename, "w", encoding="utf-8") as file:
            for dicts in list_objs:
                list_dict.append(cls.to_dictionary(dicts))
            file.write(json.dumps(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance
        with all attributes already set """

        dummy = cls(4, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances """
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
