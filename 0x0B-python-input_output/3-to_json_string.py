#!/usr/bin/python3
'''serializes objects'''


import json


def to_json_string(obj):
    '''returns the JSON rep of obj
    Args:
        obj(object): the object
    Return:
        str: JSON string of obj
    '''
    return json.dumps(obj)
