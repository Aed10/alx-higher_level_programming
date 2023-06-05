#!/usr/bin/python3
"""Module 3-rectangle"""


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
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that calculates area of a rectangle.

        Args:
            Not arguments.

        Returns:
            Area value of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Method that calculates perimeter of a rectangle.

        Args:
            Not arguments.

        Returns:
            Perimeter value of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Method that returns a rectangle by
        # character.
        (width and height)
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width + "\n") * self.__height)[:-1]
