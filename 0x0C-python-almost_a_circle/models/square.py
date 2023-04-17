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

    @property
    def size(self):
        """"""
        return self.width
    
    @size.setter
    def size(self, value):
        """"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    def update(self, *args, **kwargs):
        """"""
        if len(args) > 0 and args is not None:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attr[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
    
    def __str__(self):
        """"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)


    def to_dictionary(self):
        """"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.width
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
