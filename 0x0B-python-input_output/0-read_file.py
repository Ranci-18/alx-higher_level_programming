#!usr/bin/python3
"""defining a function"""


def read_file(filename=""):
    """function reads a text file and prints to stdout"""
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)
