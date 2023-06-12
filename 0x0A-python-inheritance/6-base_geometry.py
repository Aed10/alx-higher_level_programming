#!/usr/bin/python3
""" Module that contains a class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """Class that defines a BaseGeometry"""

    def area(self):
        """Method that raises an Exception with the message area() is not
        implemented
        """
        raise Exception("area() is not implemented")
