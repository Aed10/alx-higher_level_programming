#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nb_elements = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            nb_elements += 1

    except BaseException:
        pass
    print("")
    return nb_elements


def main():
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))


main()
