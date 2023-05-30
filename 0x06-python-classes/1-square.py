#!/usr/bin/python3

"""Create a class Square with private instance attribute size"""


class Square:
    """The Square object"""

    def __init__(self, size=0):
        """Init Square

        Args:
        size (int): size of the square.

        """
        self.__size = size
