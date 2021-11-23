#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints a matrix'''
    for item in matrix:
        if type(item) == list:
            if len(item) == 0:
                print("")
            for i in item:
                if item.index(i) == len(item) - 1:
                    print("{:d}".format(i))
                else:
                    print("{:d} ".format(i), end='')
        else:
            print("{:d}".format(item))
