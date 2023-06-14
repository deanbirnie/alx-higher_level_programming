#!/usr/bin/python3
"""Defines a function which adds an attribute to an object"""


def add_attribute(obj, attr, value):
    """Attemp to add an attribute to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
