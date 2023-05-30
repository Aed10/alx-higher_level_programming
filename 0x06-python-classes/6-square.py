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
        """Print the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

        @property
        def position(self):
            """Get/set the current position of the square."""
            return self.__position

        @position.setter
        def position(self, value):
            """Set the position of the square."""
            if type(value) is not tuple or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            if type(value[0]) is not int or value[0] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            if type(value[1]) is not int or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
