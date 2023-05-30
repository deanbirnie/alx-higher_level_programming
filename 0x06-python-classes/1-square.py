#!/usr/bin/python3

"""Create a class Square with private instance attribute size"""


class Square:
    """The Square object"""

    def __init__(self, size=0):
        """Init Square

        Args:
        size (int): size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("value entered for size is not an integer")
        elif size < 0:
            raise ValueError("size cannot be less than 0")
        self.__size = size
