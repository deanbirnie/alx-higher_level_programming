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
