#!/usr/bin/python3

import json


class Base:
    """
    A foundational class serving as the base for other classes within
    the Python Almost Circle Project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of the 'Base' class.

        Args:
            id (int, optional): An identifier for the object.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries in [None, []]:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            cls (class): The class for which to save objects.
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string to be converted.

        Returns:
            list: A list of dictionaries extracted from the JSON string.
        """
        if json_string in [None, []]:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes based on a dictionary.

        Args:
            dictionary (dict): A dictionary containing attribute values.

        Returns:
            instance: An instance of the class with
                attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
