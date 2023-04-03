#!/usr/bin/python3
"""creating a class Rectangle"""


class Rectangle:
    """Class Rectangle representing a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of object
        Attributes: width and height
        """
        self.__width = width
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

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

    def area(self):
        """Method computes the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Method computes the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
