#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


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
            return "[]"
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
        if json_string in [None, "[]"]:
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

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file with the class name as the filename.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
            data = cls.from_json_string(json_str)
            instances = [cls.create(**item) for item in data]
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
                turt.hideturtle()

            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()

            turtle.exitonclick()
