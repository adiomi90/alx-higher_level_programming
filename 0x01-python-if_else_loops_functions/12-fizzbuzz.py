#!/usr/bin/python3
def fizbuzz():
    for x in range(1, 101):
        if x % 5 == 0 and x % 3 == 0:
            print("fizzBuzz ", end="")
        elif x % 3 == 0:
            print("fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(x), end="")
