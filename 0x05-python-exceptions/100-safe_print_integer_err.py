#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
        except Exception as err:
            sys.stderr.write("Exception: {}\n".format(err))
            return False
        else:
            return True
