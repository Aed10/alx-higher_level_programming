#!/usr/bin/python3
""" Module that contains a class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """Class that defines a BaseGeometry"""

    def area(self):
        """Method that raises an Exception with the message area() is not
        implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value
        Args:
            name: name of the value
            value: value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
