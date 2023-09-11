#!/usr/bin/python3
""" Module that contains a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a Rectangle (inherits from BaseGeometry (7-
    base_geometry.py). (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        """Initializer function for a Rectangle.
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        Attributes:
            __width: width of the Rectangle
            __height: height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Method that returns a string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Method that returns the area of the Rectangle"""
        return self.__width * self.__height
