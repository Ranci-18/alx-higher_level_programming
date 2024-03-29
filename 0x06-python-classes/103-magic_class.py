#!/usr/bin/python3
"""definition of MagicClass"""
import math


class MagicClass:
    """MagicClass performs some operations
    """
    def __init__(self, radius=0):
        """New instance of MagicClass

        Attributes: radius
        """
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    @property
    def radius(self):
        """returns the radius
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """sets the radius of MagicClass
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """Method computes the area of MagicClass
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Method computes circumference of MagicClass
        """
        return 2 * math.pi * self.__radius
