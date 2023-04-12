#!/usr/bin/python3
"""defining a function"""


import json


def to_json_string(my_obj):
    """function serializes python obj to json string
    Returns:
        json string
    """
    return json.dumps(my_obj)
