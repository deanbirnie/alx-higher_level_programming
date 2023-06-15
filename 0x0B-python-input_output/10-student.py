#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initialise the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of the student"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if
                    hasattr(self, attr)}
