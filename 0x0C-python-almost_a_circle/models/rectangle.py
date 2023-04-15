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
        """"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        """"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """"""
        return self.__width * self.__height

    def display(self):
        """"""
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
        """"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"""
        if args is not None and len(args) != 0:
            attr_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
