#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for j in item:
            if (j != item[-1]):
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="\n")
