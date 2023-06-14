#!/usr/bin/python3
"""checks if object is an instance inherited attributes and methods fr0m the
specified class or not
"""


def inherits_from(obj, a_class):
    """true if object is an instance of a class that inerited (directly or
    indirectly) from the specified class; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
