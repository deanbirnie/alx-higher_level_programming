#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """The square"""

    def __init__(self, size=0):
        """instantiate a new square

        Args:
        size (int): the size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size property setter

        Args:
        value (int): the vlue for the size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of the square
        """
        return self.__size * self.__size
