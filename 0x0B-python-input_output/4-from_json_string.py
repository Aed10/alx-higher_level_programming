#!/usr/bin/python3
""" A module contains a function that returns an
object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    A function that returns an Python object represented by JSON string.

    Args:
        @my_str: A JSON string.

    Return:
        Python object.
    """
    return json.loads(my_str)
