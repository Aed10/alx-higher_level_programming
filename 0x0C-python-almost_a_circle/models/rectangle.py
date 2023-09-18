#!/usr/bin/python3

""" Define the Rectangle class, which inherits from Base """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class: Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance.

        area(self):
            Calculates the area of the rectangle.

        display(self):
            Displays the rectangle using '#' characters.

        __str__(self):
            Returns a string representation of the rectangle.

        update(self, *args, **kwargs):
            Updates the attributes of the rectangle with new values.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle using '#' characters.
        If the 'y' coordinate is not 0,
        it adds newline characters to adjust the position.
        """
        if self.y != 0:
            print("\n" * (self.y - 1))
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
                {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle with new values.

        Args:
            *args: Variable-length positional arguments.
            **kwargs: Variable-length keyword arguments.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
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
                - "width" (int): The width attribute of the instance.
                - "height" (int): The height attribute of the instance.
                - "x" (int): The x-coordinate attribute of the instance.
                - "y" (int): The y-coordinate attribute of the instance.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
