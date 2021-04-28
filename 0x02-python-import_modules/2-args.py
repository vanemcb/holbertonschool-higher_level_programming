#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    str = "arguments:"
    size = len(sys.argv)

    if size == 2:
        str = "argument:"
    elif size == 1:
        str = "arguments."
    print("{} {}".format(size - 1, str))

    for i in range(1, size):
        print("{}: {}".format(i, sys.argv[i]))
