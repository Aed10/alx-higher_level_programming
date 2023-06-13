#!/usr/bin/python3
"""From JSON string to Object"""


import json


def from_json_string(my_str):
    """Return object represented by JSON string my_str"""
    return json.loads(my_str)
