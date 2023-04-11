#!/usr/bin/python3
"""Defining a subclass"""


class MyList(list):
    """Subclass MyList of superclass list
    """
    def print_sorted(self):
        """Method prints sorted list
        """
        list = self[:]
        print(sorted(list))
