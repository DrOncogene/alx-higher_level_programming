#!/usr/bin/python3
'''deserializes a JSON string from a JSON file'''
import json


def load_from_json_file(filename):
    '''creates an object from a JSON file
    Args:
        filename(str): the file
    Return:
        object: the deserilized object
    '''
    with open(filename, "r") as f:
        return json.loads(f.read())
