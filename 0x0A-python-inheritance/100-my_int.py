#!/usr/bin/python3
"""defining a subclass"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, value):
        """Instantiation"""
        super().__init__()
        self.value = value

    def __eq__(self, other):
        """Not equal to method"""
        return self.value != other

    def __ne__(self, other):
        """Inverted not equal to method"""
        return self.value == other
