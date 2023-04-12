#!/usr/bin/python3
"""defining a function"""


import json


def save_to_json_file(my_obj, filename):
    """function writes json rep of my_obj to filename using with"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
