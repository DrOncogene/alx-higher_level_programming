#!/usr/bin/python3
'''deserializes objects'''


import json


def from_json_string(my_str):
    '''returns the obj from a JSON string
    Args:
        my_str(str): the object
    Return:
        object: the desrialized object
    '''
    return json.loads(my_str)
