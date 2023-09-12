#!/bin/usr/python3
"""Module that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file.


    Args:
        @filename: A JSON file.

    Return:
        A Python Object.
    """
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.loads(json_file)

