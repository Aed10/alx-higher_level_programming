#!/usr/bin/python3
# 8-rectangle.py

""" A Class called Rectangle. """


class Rectangle:
    """A Rectangle Class.

    Public class attribute:
        number_of_instances(int): count the number of Class instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object.

        Args:
            width (int): A private attribute representing
                the width of the rectangle.
            height (int): A private attribute representing
                the height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public method called Area.

        Return:
            The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """A public method called êrimeter.

        Return:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the Rectangle Object."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"

        return rectangle_str[:-1]

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method to perform cleanup tasks."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to compare two Rectangles based on their area.

        Args:
            rect_1(Rectangle): The first rectangle.
            rect_2(Rectangle): The seond rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
                return rect_1
            return rect_2
