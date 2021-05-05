#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 0:
        number1 = tuple_b[0]
        number2 = tuple_b[1]
    elif len_b == 0:
        number1 = tuple_a[0]
        number2 = tuple_a[1]
    elif len_a == 0 and len_b == 0:
        return tuple_c = ()
    elif len_a < 2:
        number1 = tuple_a[0] + tuple_b[0]
        number2 = tuple_a[0] + tuple_b[1]
    elif len_b < 2:
        number1 = tuple_a[0] + tuple_b[0]
        number2 = tuple_a[1] + tuple_b[0]
    else:
        number1 = tuple_a[0] + tuple_b[0]
        number2 = tuple_a[1] + tuple_b[1]

    tuple_c = (number1, number2)
    return tuple_c
