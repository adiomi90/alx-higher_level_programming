#!/usr/bin/python3
if __name__ == "__main__":
    from sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))
    for x in range(count):
        print("{:d}: {:d}".format(x + 1, sys.argv[x + 1]))
