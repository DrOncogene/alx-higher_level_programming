#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lst in matrix:
        new_matrix.append([x**2 for x in lst])
    return new_matrix
