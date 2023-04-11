#!/usr/bin/python3
"""defining a function"""


def inherits_from(obj, a_class):
    """function checks object relation to superclass"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
