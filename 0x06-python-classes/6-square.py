#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    class Square defining a square of 'size'

    Attributes: size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        creates first instance of Square

        Attributes: size and position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """public method computing the area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method to return the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the object of square object

        Raises:
            TypeError
            ValueError
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Method returns the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method sets the position

        Attributes: positive tuple

        Raises: TypeError for failed conditions
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1] != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Method prints a square of '#' characters according to size
        and position given
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                print("#" * (self.__size))
