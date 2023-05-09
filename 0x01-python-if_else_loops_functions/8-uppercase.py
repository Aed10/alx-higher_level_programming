#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            if i == len(str) - 1:
                sp = "\n"
            else:
                sp = ""
            print("{:c}".format(ord(str[i]) - 32), end=sp)
        else:
            if i == len(str) - 1:
                sp = "\n"
            else:
                sp = ""
            print("{:c}".format(ord(str[i])), end=sp)
