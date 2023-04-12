#!/usr/bin/python3
"""defining a function"""


def write_file(filename="", text=""):
    """function writes a string to a text file
    Returns:
        number of bytes written
    """
    with open(filename, 'w') as f:
        return f.write(text)
