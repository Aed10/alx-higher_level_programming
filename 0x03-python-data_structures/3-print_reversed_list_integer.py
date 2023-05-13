#!/usr/bin/python3
"""Function that prints all integers of a list in reverse order."""


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list), 0, -1):
        print("{:d}".format(my_list[i - 1]))


# q: what i did wrong
# a: i did not use the correct syntax for the range function
# q: what is the right syntax for range function


def main():
    print_reversed_list_integer([1, 2, 3, 4, 5])
    print_reversed_list_integer([1, 2])
    print_reversed_list_integer([4, 5, 6, 7, 8, 9, 10])
    print_reversed_list_integer()
    print_reversed_list_integer([1])


if __name__ == "__main__":
    main()
