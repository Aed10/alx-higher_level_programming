#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the current area of the square"""
        return self.__size**2

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
            return
        for x in range(self.position[1]):
            print()
        for x in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
        """
        prints a square of hashtags based on position and size
        """

    @property
    def position(self):
        return self.__position
        """
        gets position
        """

    @position.setter
    def position(self, value):
        if (
            type(value) is not tuple
            or len(value) is not 2
            or type(value[0]) is not int
            or type(value[1]) is not int
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

        """
        sets position
        position has to be a tuple of positive integers
        Raise:
            ValueError
            TypeError
        """
