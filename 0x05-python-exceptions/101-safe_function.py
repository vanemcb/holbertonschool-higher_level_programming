#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except ValueError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
    except TypeError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
    except NameError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
    except ZeroDivisionError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
    except IndexError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(None)
