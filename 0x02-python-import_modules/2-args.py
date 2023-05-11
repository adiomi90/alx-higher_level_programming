#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    if count == 1:
        print("0 argument.")
    elif count == 2:
        print("1 argument.")
    else:
        print("{:d} arguments:".format(count - 1))

    for x in range(1, count):
        print("{:d} : {:d}".format(x, argv[x))
