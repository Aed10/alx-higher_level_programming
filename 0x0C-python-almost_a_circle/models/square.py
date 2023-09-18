#!/usr/bin/python3
"""Defines a square model class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class: Represents a square, which is a specific type of rectangle.

    Attributes:
        size (int): The size of the square (both width and height).
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier for the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a new Square instance.

        __str__(self):
            Returns a string representation of the square.

        update(self, *args, **kwargs):
            Updates the attributes of the square with new values.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square (both width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (both width and height)."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square with new values.

        Args:
            *args: Variable-length positional arguments.
            **kwargs: Variable-length keyword arguments.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Convert the attributes of an instance to a dictionary.

        Returns:
            dict: A dictionary containing the attributes of the instance.
                - "id" (int): The identifier of the instance.
                - "size" (int): The size of the instance.
                - "x" (int): The x-coordinate attribute of the instance.
                - "y" (int): The y-coordinate attribute of the instance.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
