#!/usr/bin/python3
"""creating a class Rectangle
Class recreates an actual rectangle with its most basic attributes
"""


class Rectangle:
    """Class Rectangle representing a rectangle
    Attributes:
    width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation of object
        Attributes:
        width and height

        Raises:
            typeerror and valueerror
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
        type(self).number_of_instances += 1

    @property
    def width(self):
        """property getter for width
        Returns:
        instance width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width
        Raises:
            typeerror and valueerror
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property getter for height
        Returns:
            height of instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height
        Raises:
            typeerror and valueerror
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method computes the area of the rectangle

        Returns:
            area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Method computes the perimeter of the rectangle

        Returns:
            perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string method representation of rectangle

        Returns:
            string ready to print
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for i in range(self.__height))

    def __repr__(self):
        """method returns string representation of rectangle

        Returns: string for recreation
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """method deletes object instance
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method compares two rectangles by area

        Returns:
            largest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method that returns a square

        Returns: square
        """
        return cls(size, size)
