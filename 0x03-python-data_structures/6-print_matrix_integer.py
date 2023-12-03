#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(matrix):
        for j in range(matrix[i]):
            if (j != 0):
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="\n")
