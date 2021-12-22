#!/usr/bin/python3
'''appends to a file'''


def append_write(filename="", text=""):
    '''append text to filename
    Args:
        filename(str): name of file
        text(str): the string to write to file
    Return:
        int: the number of char written
    '''
    with open(filename, "a") as f:
        return f.write(text)
