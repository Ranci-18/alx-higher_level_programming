#!/usr/bin/python3
"""defining a class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle
    Attributes:
            size
            x
            y
            id
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
