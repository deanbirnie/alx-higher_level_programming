#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create the object from JSON file"""
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
