#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nb_elements = 0
    for i, element in enumerate(my_list):
        if i < x:
            try:
                print("{}".format(element), end="")
                nb_elements += 1
            except BaseException:
                pass
    print("")
    return nb_elements
