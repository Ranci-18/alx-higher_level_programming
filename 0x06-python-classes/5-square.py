#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    class Square defining a square of 'size'

    Attributes: size
    """
    def __init__(self, size=0):
        """
        creates first instance of Square

        Args: size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

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

    def my_print(self):
        """
        Method prints a square of '#' characters according to size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
