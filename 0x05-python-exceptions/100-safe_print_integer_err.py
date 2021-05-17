#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return(True)
    except ValueError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(False)
    except TypeError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(False)
