#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    prod = 0
    total = 0

    for item in my_list:
        prod += item[0] * item[1]
        total += item[1]
    return prod / total
