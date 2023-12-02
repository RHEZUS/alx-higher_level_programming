#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for j in item:
            print("{:d}".format(j), end=" ")
        print()
