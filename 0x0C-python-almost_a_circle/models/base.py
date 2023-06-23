#!/usr/bin/python3
"""Class Base"""

import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Class Base"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class Base"""
        if list_objs is None:
            list_objs = []
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Class Base"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
