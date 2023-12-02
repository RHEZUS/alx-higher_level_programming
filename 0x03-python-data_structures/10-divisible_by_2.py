#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    result += my_list
    for i in range(len(my_list)):
        result[i] = i % 2 == 0
    return result
