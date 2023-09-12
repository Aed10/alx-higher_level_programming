#!/usr/bin/python3

"""A module that contains a function that appends
    a string at the end of a text file."""


def append_write(filename="", text=""):
    """
    A function to append a text file at the end of a text file.

    Args:
        @filename: A given file.
        @text: The data that we want to add to the end of the file.

    Return:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
