#!/usr/bin/python3
""" Module that contains a class Square that inherits from Rectangle
    (9-rectangle.py). (task based on 10-square.py).
    (task based on 4-inherits_from.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square (inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py). (task based on 4-inherits_from.py)"""

    def __init__(self, size):
        """Initializer function for a Square.
        Args:
            size: size of the Square
        Attributes:
            __size: size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method that returns the area of the Square"""
        return self.__size**2

    def __str__(self):
        """Method that returns a string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
