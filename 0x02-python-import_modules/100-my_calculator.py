#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ['+', '-', '*', '/']
    if not sys.argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    if (sys.argv[2] == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if (sys.argv[2] == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if (sys.argv[2] == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
