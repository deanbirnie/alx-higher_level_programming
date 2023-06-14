#!/usr/bin/python3
"""Define a square with Ractangle as the base class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining a square with ectangle as the base case"""

    def __init__(self, size):
        """Initialise a square"""
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
