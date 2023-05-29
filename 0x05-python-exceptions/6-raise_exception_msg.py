#!/usr/bin/pyrhon3
def raise_exception_msg(message=""):
    raise NameError(message)


def main():
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)


if __name__ == "__main__":
    main()
