#!/usr/bin/python3
# 1-rectangle.py

""" A Class called Rectangle. """


class Rectangle:
    """A Rectangle Class."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object.

        Args:
            width (int): A private attribute representing
                the width of the rectangle.
            height (int): A private attribute representing
                the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
