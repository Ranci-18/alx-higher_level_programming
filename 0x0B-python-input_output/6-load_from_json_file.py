#!/usr/bin/python3
"""defining a function"""


import json


def load_from_json_file(filename):
    """function creates a python object from jsonfile"""
    with open(filename, 'r') as f:
        contents = f.read()
        json.loads(contents)
