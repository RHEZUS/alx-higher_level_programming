#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for j in range(len(item)):
            if (j < len(item) - 1):
                print("{}".format(item[j]), end=" ")
            else:
                print("{}".format(item[j]), end="\n")
