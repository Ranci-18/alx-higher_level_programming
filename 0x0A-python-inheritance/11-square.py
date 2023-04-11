#!/usr/bin/python3
"""defining a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square

    Attributes:
        size
    """
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """computes area of class Square"""
        return self.__size ** 2

    def __str__(self):
        """Returns string to print"""
        return "[Square] {}/{}".format(self.__size, self.__size)
