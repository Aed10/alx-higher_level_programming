#!/usr/bin/python3
""" Module that contains a function that returns the list of available
    attributes and methods of an object """


def lookup(obj):
    """Function that returns the list of available attributes and methods
        of an object

    Args:
        obj: object to look up

    Returns:
        list: list of available attributes and methods
    """
    return dir(obj)
