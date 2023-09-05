#!/usr/bin/python3

""" Copy a list object. """


def copy_list(orig_list):
    """Copy a list.

    Args:
        l(list): list to be copied.

    Return:
        A copy of list l
    """
    l_cpy = orig_list.copy()
    return l_cpy
