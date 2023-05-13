#!/usr/bin/python3
"""Function that replaces an element in a list at a specific position"""


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list[idx] = element
    return new_list
