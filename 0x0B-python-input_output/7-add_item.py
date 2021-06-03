#!/usr/bin/python3
""" Script that adds all input_list to a Python list,
and then save them to a file """
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

input_list = argv[1:]
try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []

for element in input_list:
    my_list.append(element)

save_to_json_file(my_list, "add_item.json")
