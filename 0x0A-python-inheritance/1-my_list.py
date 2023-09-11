#!/usr/bin/python3
""" Module that contains a Class MyList that inherits from list """


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
