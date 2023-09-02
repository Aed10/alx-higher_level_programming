#!/usr/bin/python3
# 0-add_integer.py

"""
 This module contain a function that adds two integers,
 and return theire sum.

 Author: ED DYYANY Ayoub
"""


def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a: An int or float.
        b: int or float.

    Returns:
        int: The sume of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
