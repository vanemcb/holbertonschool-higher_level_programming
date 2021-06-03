#!/usr/bin/python3
""" Module to create function save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
