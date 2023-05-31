#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__"""
        self.size = size
        self.position = position

    def area(self):
        """area"""
        return self.__size**2

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(i) is not int for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """my_print"""
        if self.__size == 0:
            return ""
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(
                    "{}{}".format(" " * self.__position[0], "#" * self.__size)
                )
            return "{}{}".format(" " * self.__position[0], "#" * self.__size)


def main():
    """main"""
    my_square = Square(3, (1, 1))
    my_square.my_print()
    my_square = Square(5, (3, 2))
    my_square.my_print()


if __name__ == "__main__":
    main()
