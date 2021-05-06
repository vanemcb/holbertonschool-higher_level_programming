#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_keys = sorted(a_dictionary.keys())
    for key in a_keys:
        print('{}: {}'.format(key, a_dictionary[key]))
