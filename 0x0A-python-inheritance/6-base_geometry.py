#!/usr/bin/python3
"""Raises an exception in the method area()"""


class BaseGeometry:
    """base class"""

    def area(self):
        """area raises an exception"""
        raise Exception("area() is not implemented")
