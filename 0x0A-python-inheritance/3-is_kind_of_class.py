#!/usr/bin/python3
"""checks if an object is an instance of a class or a class that inherited
 attribute and methods fr0m the specified class.
"""


def is_kind_of_class(obj, a_class):
    """True if the object is an instance of a class or inherits fr0m
    the specified class, otherwise False
    """
    return isinstance(obj, a_class)
