#!/usr/bin/python3
"""Module 6-rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    # A class variable, counting the number of rectangles
    number_of_instances = 0
    # A class variable, to change the print symbol
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init method to initialized a instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        """
        self.width = width
        self.height = height
        # Every time a new instance is created, increment
        # the class variable
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method getter for width atributte.

        Args:
            Not arguments.

        Returns:
            Width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method setter for width atributte.

        Args:
            value (int): width value of the rectangle.

        Returns:
            Always nothing.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method getter for height atributte.

        Args:
            Not arguments.

        Returns:
            Height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method setter for height atributte.

        Args:
            value (int): height value of the rectangle.

        Returns:
            Always nothing.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that calculates area of a rectangle.

        Args:
            Not arguments.

        Returns:
            Area value of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Method that calculates perimeter of a rectangle.

        Args:
            Not arguments.

        Returns:
            Perimeter value of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Method that returns a rectangle by
        # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(
                "{}".format(self.print_symbol) * self.width
                for x in range(self.height)
            )

    def __repr__(self):
        """Method that returns a string representation
        of a rectangle to be able to recreate a new
        instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method that delete a instance of rectangle."""
        # Every time a new instance is deleted, decrement
        # the class variable
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle based
        on the area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Returns:
            The rectangle with the biggest area, or rect_1
            if both have the same area.

        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method that returns a new Rectangle instance
        with width == height == size.

        Args:
            size (int): Size of the new rectangle.

        Returns:
            A new instance of Rectangle with width == height == size.

        """
        return cls(size, size)
