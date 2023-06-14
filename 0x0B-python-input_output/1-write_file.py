#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """write the given string to a text file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        characters_written = file.write(text)
    return characters_written
