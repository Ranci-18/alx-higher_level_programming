#!/usr/bin/python3
"""defining a function"""


def class_to_json(obj):
    """function returns dictionary description with simple
    data structure"""
    return obj.__dict__
