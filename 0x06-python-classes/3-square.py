#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """The square"""

    def __init__(self, size=0):
        """instantiate a new square

        Args:
        size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of the square
        """
        return self.__size * self.__size
