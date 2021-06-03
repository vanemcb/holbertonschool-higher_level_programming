#!/usr/bin/python3
""" Module to create function write_file """


def write_file(filename="", text=""):
    """ Function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        num_char = file.write(text)
    return num_char
