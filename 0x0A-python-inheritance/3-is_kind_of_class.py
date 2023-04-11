#!/usr/bin/python3
"""defining a function"""


def is_kind_of_class(obj, a_class):
    """function checks if an object is
    of a superclass or subclass

    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
