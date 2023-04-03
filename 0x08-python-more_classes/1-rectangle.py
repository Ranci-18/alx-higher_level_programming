#!/usr/bin/python3
"""creating a class Rectangle"""


class Rectangle:
    """Class Rectangle representing a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of object
        
        Attributes: width and height
        """
        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """property setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
