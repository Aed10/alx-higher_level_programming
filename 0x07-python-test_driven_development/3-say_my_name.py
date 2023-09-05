#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """Function to print a full name.

    Args:
        first_name(str): The first name of a user.
        last_name(str): The last name if a user.

    Reutn:
        Print the full name of a user.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
