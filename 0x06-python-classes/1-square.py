#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("value entered for size is not an integer")
        elif size < 0:
            raise ValueError("size cannot be less than 0")
        self.__size = size
