#!/usr/bin/python3

""" This module contains a function that returns tje JSON
representation of a nobject.
"""
import json


def to_json_string(my_obj):
    """
    A function to convert a Python data into a JSON-formatted string.

    Args:
        my_obj: A Python data.

    Return:
        A JSON-format.
    """

    return json.dumps(my_obj)
