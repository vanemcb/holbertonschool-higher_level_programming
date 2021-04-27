#!/usr/bin/python3
for number in range(0, 99):
    print("{}".format(str(number).zfill(2)), end=", ")
print("{}".format(number + 1))
