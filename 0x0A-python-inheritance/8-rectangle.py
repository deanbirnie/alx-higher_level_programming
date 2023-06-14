#!/usr/bin/python3
"""Import 7-base_geometry for base case"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining a rectangle"""

    def __init__(self, width, height):
        """Initialising the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
