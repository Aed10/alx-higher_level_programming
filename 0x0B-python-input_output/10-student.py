#!/usr/bin/python3
"""Module that creates a Student class (based on 9-student.py)"""


class Student:
    """Creates a Student class (based on 9-student.py)"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student class (based on 9-student.py)"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            self.__dict__[key] = json[key]
