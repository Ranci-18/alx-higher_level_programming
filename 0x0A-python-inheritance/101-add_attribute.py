#!/usr/bin/python3
"""Defining a function"""


def add_attribute(obj, attr1, attr2):
    """Function to add an attribute to object"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr1, attr2)
