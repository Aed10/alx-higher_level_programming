#!/bin/usr/python3

import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file.


    Args:
        @filename: A JSON file.

    Return:
        A Python Object.
    """
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data
