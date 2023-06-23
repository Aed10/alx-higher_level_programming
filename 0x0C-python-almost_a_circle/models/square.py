#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Class Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Class Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Class Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Class Square"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Class Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
