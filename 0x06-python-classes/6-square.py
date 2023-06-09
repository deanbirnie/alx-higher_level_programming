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

    def __str__(self):
        self.my_print()

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

        Args:
        value (tuple): set of 2 positive integers representing position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
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
