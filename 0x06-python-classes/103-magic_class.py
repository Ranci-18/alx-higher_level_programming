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
            raise TypeError("Radius must be a number")
        self.__radius = radius

    def area(self):
        """Method computes the area of MagicClass
        """
        result_area = math.pi * self.__radius ** 2
        return result_area

    def circumference(self):
        """Method computes circumference of MagicClass
        """
        result_circumference = math.pi * self.__radius * 2
        return result_circumference
