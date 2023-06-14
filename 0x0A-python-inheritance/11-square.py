#!/usr/bin/python3
"""defines a square base case - Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defining the square object"""

    def __init__(self, size):
        """Initialising a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
