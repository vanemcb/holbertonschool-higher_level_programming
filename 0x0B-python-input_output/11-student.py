#!/usr/bin/python3
""" Class Student module """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dict_filtered = {}
        for key, value in self.__dict__.items():
            for a in attrs:
                if a == key:
                    dict_filtered[key] = value
        return dict_filtered

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
