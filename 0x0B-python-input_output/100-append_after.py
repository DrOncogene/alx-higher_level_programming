#!/usr/bin/python3
'''searches a file and adds a line of text a given point'''


def append_after(filename="", search_string="", new_string=""):
    '''searches filename for search_string and append new_string after
    any lines that contains it
    Args:
        filename(str): the file
        search_string(str): string to look for
        new_string(str): string to append to the file
    Return: nothing
    '''
    with open(filename, "r") as f:
        content = f.read()

    with open(filename, "r+") as f:
        matches = []
        while f.tell() < len(content):
            line = f.readline()
            if search_string in line:
                matches.append(f.tell())
        for i in range(len(matches)):
            if i == 0:
                pos = matches[i]
            else:
                pos = matches[i] + (len(new_string) * i)
            first_part = content[:pos]
            first_part += new_string
            second_part = content[pos:]
            content = first_part + second_part
        f.seek(0)
        f.truncate()
        f.write(content)
