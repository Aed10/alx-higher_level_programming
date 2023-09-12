#!/usr/bin/python3
"""A module that contains a function that write a string to a text file."""


def write_file(filename="", text=""):
    """
    A function to write a string text to agiven file.

    Args:
        @filename: A given file.
        @text: The text that we wnat to add to @filename.

    Return:
        count: Thenumber of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
