#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
    print()
    file.close()


if __name__ == "__main__":
    read_file("my_file_0.txt")
