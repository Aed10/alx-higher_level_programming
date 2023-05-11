# /usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    sum = 0
    if argc == 1:
        print("0")
    else:
        for i in range(1, argc):
            sum += int(sys.argv[i])
        print("{}".format(sum))
