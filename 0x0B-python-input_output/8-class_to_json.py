#!/usr/bin/python3
"""Define a function that returns a dictionary description with simple data
structure for JSON serialisation of an object"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
