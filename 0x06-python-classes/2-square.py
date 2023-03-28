#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    class Square defining a square of 'size'

    Attributes: size
    """
    def __init__(self, size=0):
        """
        creates first instance of Square

        Args: size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
