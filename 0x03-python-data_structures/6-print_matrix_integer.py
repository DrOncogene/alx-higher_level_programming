#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints a matrix'''
    if len(matrix) == 0:
        print("")
    for item in matrix:
        if type(item) == list:
            for i in item:
                if item.index(i) == len(item) - 1:
                    print("{:d}".format(i))
                else:
                    print("{:d} ".format(i), end='')
        else:
            print("{:d}".format(item))
