#!/usr/bin/python3
def uppercase(str):
    lower_case = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
                  109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                  121, 122]
    for letter in str:
        if ord(letter) in lower_case:
            letter = chr(lower_case[lower_case.index(ord(letter))] - 32)
        print("{}".format(letter), end="")
    print("{}".format(""))
