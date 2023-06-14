#!/usr/bin/python3
"""Reading from a text file"""


def read_file(filename=""):
    """Print the text from the specified file"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
