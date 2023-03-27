#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
            return True
        except ValueError:
            sys.stderr.write(
                "Exception: Unknown format "
                "code 'd' for object of type 'str'\n")
            return False
    else:
        sys.stderr.write(
            "Exception: Uknown format "
            "code 'd' for object of type 'str'\n")
        return False
