#!/usr/bin/python3
'''writes to a file'''


def write_file(filename="", text=""):
    '''writes text to filename
    Args:
        filename(str): name of file
        text(str): the string to write to file
    Return:
        int: the number of char written
    '''
    with open(filename, "w") as f:
        return f.write(text)
