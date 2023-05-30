#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """The square"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiate a new square

        Args:
        size (int): the size of the new square
        position (int, int): position of new square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """use # to print out the square
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
