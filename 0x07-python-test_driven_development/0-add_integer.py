#!/usr/bin/python3
"""
    Function add_integer module
"""


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
        The add of a and b.

    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
