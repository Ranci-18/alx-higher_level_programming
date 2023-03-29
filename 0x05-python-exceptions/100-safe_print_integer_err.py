#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
            return True
        except ValueError as err:
            sys.stderr.write("Exception: {}\n".format(err))
            return False
        except TypeError:
            sys.stderr.write("Exception: unsupported format string passed to set.__format__\n")
            return False
