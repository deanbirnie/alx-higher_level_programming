#!/usr/bin/python3
"""Returns a list of all available attributes and methods of an object"""


def lookup(obj):
    """Looks for all attributes and methods of an object"""
    return dir(obj)
