#!/usr/bin/python3
'''reads a file and prints in on stdout'''


def read_file(filename=""):
    '''reads a text file
    Args:
        filename(str): name of file
    Return: nothing
    '''
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    with open(filename, "r") as f:
        print(f.read(), end='')
