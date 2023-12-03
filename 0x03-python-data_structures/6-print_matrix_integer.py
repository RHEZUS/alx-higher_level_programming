#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(matrix):
        for j in range(matrix[i]):
            if (j != 0):
                print(" ", end="")
            print("{:d}".format(matrix[i][j]), end="\n")
        print()
