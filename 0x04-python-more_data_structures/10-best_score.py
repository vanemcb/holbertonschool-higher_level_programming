#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_max_value = max(a_dictionary, key=a_dictionary.get)
    return key_max_value
