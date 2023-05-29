#!/usrbin/python3

def safe_print_list(my_list=[], x=0):

    nb_print = 0
    try:
        for index in range(0, x):
            print(my_list[index], end='')
            nb_print += 1
        print()

    except IndexError:
        print()

    return nb_print
