#!/usr/bin/python3

for n in range(0, 9):
    for n2 in range(0, 10):
        if n < n2 and n != 8:
            print("{}{}".format(n, n2), end=", ")
print("{}{}".format(n, n2))
