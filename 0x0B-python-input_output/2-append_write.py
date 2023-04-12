#!/usr/bin/python3
"""defining a function"""


def append_write(filename="", text=""):
    """function appends text to filename even if filename does not exist
    Returns:
        number of characters appended
    """
    with open(filename, 'a') as f:
        return f.write(text)
