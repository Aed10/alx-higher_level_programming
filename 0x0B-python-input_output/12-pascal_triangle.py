#!/usr/bin/python3

"""Pascal's Triangle Task"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of
    integers representing the Pascal's triangle
    of n.
    """
    lists = [[]]
    if n <= 0:
        return []

    for i in range(1, n + 1):
        for j in range(0, i):
            if i == 1:
                lists[0].append(1)
            elif j == 0:
                lists.append([1])
            elif j == i - 1:
                lists[i - 1].append(1)
            else:
                lists[i - 1].append(lists[i - 2][j] + lists[i - 2][j - 1])
    return lists
