#!/usr/bin/python3
"""
    Function text_indentation module
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of
    these characters: ., ? and .

    Args:
        text: input text.

    """

    if type(text) != str:
        raise TypeError("text must be a string")

    text_final = ""
    index = 0

    while index < len(text):
        text_final = text_final + text[index]
        if text[index] == "." or text[index] == "?" or text[index] == ":":
            text_final = text_final + "\n\n"
            index += 1
        index += 1

    print(text_final, end="")
