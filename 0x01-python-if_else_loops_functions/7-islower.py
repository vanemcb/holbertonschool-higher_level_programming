#!/usr/bin/python3
def islower(c):
    for letter in range(97, 123):
        if letter == ord(c):
            return(True)
    return(False)
