#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]

    tuple_final = (len(sentence), first_char)

    return tuple_final
