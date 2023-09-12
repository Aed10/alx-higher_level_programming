#!/usr/bin/python3
"""This module contains a function that writes an Object to a text file
Using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function to writes an Object ot a text file using JSON repr.

    Args:
        @my_obj: A given object.
        @filename: A given twt file.
    """
    with open(filename, "w") as text_file:
        json.dump(my_obj, text_file)
