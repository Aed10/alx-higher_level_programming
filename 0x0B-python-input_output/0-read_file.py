#!/usr/bin/python3
"""A module contains a function that read a text file."""


def read_file(filename=""):
    """Read a text file.

    Args:
        @filename: The name of the file.

    Return:
        The contenants of the given @filename.
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
