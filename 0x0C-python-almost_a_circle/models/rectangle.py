#!/usr/bin/python3
"""Defining a class"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle
    Attributes:
        width
        height
        x
        y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of class object"""
        super().__init__(id)
        """Calling the super class with id"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise TypeError("height must be > 0")
        self.height = height

        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method computes and returns area of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Method desplays the Rectangle instance"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print('#', end="")
            print()

    def __str__(self):
        """Method retursn string to print"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Method updates attribute arguments"""
        if args is not None and len(args) != 0:
            attr_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method creates a dict of attributes and values"""
        rectangle_dict = {}
        rectangle_dict["id"] = self.id
        rectangle_dict["width"] = self.width
        rectangle_dict["height"] = self.height
        rectangle_dict["x"] = self.x
        rectangle_dict["y"] = self.y
        return rectangle_dict
