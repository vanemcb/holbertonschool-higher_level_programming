#!/usr/bin/python3
""" Module to create function write_file """


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        num_char = file.write(text)
    return num_char
