#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    mul, addition = 0, 0

    for tupl in my_list:
        mul += tupl[0] * tupl[1]
        addition += tupl[1]

    return (mul / addition)
