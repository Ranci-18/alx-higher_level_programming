#!/usr/bin/python3
"""defining a function"""


def append_after(filename="", search_string="", new_string=""):
    """function searches and appends new string
    after search string"""
    with open(filename, 'r') as f:
        content = f.readlines()

    with open(filename, 'w') as o_f:
        for line in content:
            if search_string in line:
                o_f.write(line)
                o_f.write(new_string)
            else:
                o_f.write(line)
