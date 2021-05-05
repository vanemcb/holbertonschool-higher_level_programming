#!/usr/bin/python3
def no_c(my_string):
    i = 0
    my_string2 = my_string
    for char in my_string:
        if char == 'c' or char == 'C':
            my_string2 = my_string[:i] + my_string[i + 1:]
        i += 1
    return my_string2
