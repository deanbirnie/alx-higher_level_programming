#!/usr/bin/python3
"""Define a function that converts an object (python data structure) to JSON"""
import json


def from_json_string(my_str):
    """Convert to JSON"""
    return json.loads(my_str)
