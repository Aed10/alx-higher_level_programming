#!/usr/bin/python3
""" Module that contains a class MyInt that inherits from int """


class MyInt(int):
    """Class that inherits from int"""

    def __eq__(self, other):
        """Method that returns the opposite of the equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Method that returns the opposite of the inequality"""
        return super().__eq__(other)
