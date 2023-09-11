#!/usr/bin/python3
""" Module that contains a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a Rectangle from BaseGeometry (7-base_geometry.py)"""

    def __init__(self, width, height):
        """Initializer for a Rectangle
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
