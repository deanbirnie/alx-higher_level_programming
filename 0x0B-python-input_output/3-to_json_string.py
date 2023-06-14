#!/usr/bin/python3
"""Define a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Return JSON representation of string"""
    return json.dumps(my_obj)
