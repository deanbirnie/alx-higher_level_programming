#!/usr/bin/python3
"""Define a function that writes an obect to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
