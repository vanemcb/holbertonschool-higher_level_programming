#!/usr/bin/python3
def no_c(my_string):
    my_string2 = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        my_string2 += char
    return my_string2
