#!/usr/bin/python3
"""Raises an exception in the method area()"""


class BaseGeometry:
    """base class"""

    def area(self):
        """area raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """input integer validation"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Defining a rectangle"""

    def __init__(self, width, height):
        """Initialising the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
