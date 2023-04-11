#!/usr/bin/python3
"""defining an empty class"""


class BaseGeometry:
    """Empty class"""
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
