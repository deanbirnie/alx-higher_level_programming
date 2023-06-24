#!/usr/bin/python3
"""Defining a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """updating values"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary attributes"""
        my_dict =  {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

        return my_dict
