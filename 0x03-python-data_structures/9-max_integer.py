#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    Max = my_list[0]
    for number in my_list:
        if number >= Max:
            Max = number
    return Max
