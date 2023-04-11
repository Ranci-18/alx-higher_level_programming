#!usr/bin/python3
"""defining a function"""


def lookup(obj):
    """function that returns attributes and methods of object
    Returns:
        a list of attributes and methods
    """
    list = [dir(obj)]
    return list
