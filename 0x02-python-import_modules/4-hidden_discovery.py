#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden

    for i in dir(hidden):
        if i[0] != "_":
            print(i)
