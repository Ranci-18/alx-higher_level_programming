#!/usr/bin/python3
"""Definining a function"""


def is_same_class(obj, a_class):
    """Function to check if object is an instance of a class"""
    if type(obj) == a_class:
        return True
    return False
