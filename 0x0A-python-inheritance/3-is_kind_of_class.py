#!/usr/bin/python3
"""Checks if an object is an instance of a class or a class that inherited
from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """True if the object is an instance of a class or inherits from
    the specified class, otherwise False
    """
    return isinstance(obj, a_class)
