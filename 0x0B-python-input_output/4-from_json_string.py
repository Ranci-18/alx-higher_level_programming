#!/usr/bin/python3
"""defining a function"""


import json


def from_json_string(my_str):
    """function retrieves a python object from a json string
    Returns:
        python object
    """
    return json.loads(my_str)
