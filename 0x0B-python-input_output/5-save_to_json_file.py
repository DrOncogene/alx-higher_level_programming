#!/usr/bin/python3
'''writes an object to a file in JSON format'''
import json


def save_to_json_file(obj, filename):
    '''serializes obj to filename
    Args:
        obj(object): the object
        filename(str): name of the file
    Return: nothing
    '''
    with open(filename, "w") as f:
        f.write(json.dumps(obj))
