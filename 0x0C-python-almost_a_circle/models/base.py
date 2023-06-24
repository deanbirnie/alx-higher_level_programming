#!/usr/bin/python3
"""This module is a base for other classes"""

import json


class Base:
    """Base class for all classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation"""

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
