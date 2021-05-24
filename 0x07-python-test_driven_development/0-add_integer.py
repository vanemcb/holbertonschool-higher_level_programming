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

    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
