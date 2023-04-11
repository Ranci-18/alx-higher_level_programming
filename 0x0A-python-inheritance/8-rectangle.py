#!/usr/bin/python3
"""defining an empty class and subclass"""


class BaseGeometry:
    """Empty class"""
    def __init__(self):
        pass

    def area(self):
        """Method raise Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates value

        Raise:
            TypeError
            ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Subclass Rectangle

        Attributes:
            width and height
    """
    def __init__(self, width, height):
        """Instantiation"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
