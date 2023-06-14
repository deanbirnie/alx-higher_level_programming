#!/usr/bin/python3
"""Define a function that appends text to a text file"""


def append_write(filename="", text=""):
    """Appends the given text to the specified text file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        characters_added = file.write(text)
    return characters_added
