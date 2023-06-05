#!/usr/bin/python3
"""Module 1-rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Init method to initialized a instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method getter for width atributte.

        Args:
            Not arguments.

        Returns:
            Width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method setter for width atributte.

        Args:
            value (int): width value of the rectangle.

        Returns:
            Always nothing.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method getter for height atributte.

        Args:
            Not arguments.

        Returns:
            Height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method setter for height atributte.

        Args:
            value (int): height value of the rectangle.

        Returns:
            Always nothing.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value
