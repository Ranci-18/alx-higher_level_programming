#!/usr/bin/python3
"""defining a class"""


class Base:
    """Class Base
    Attributes:
        private class attribute
        id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """instantiation of class object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
