#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''adds two tuples'''
    if len(tuple_a) == 1:
        tuple_a[1] = 0
    elif len(tuple_a) == 0:
        tuple_a = 0, 0
    if len(tuple_b) == 1:
        tuple_b[1] = 0
    elif len(tuple_b) == 0:
        tuple_b = 0, 0
    a, b = tuple_a[0], tuple_a[1]
    c, d = tuple_b[0], tuple_b[1]
    res = a+c, b+d

    return res
