#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, num in a_dictionary.items():
        new_dictionary[key] = num * 2
    return new_dictionary
