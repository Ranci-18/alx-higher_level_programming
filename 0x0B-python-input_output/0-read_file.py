#!/usr/bin/python3
"""defining a function"""


def read_file(filename=""):
    """function reads a text file and prints to stdout"""
    with open(filename, 'r') as UTF8:
        contents = UTF8.read()
        print(contents)
