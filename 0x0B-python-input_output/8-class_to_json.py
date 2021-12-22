#!/usr/bin/python3
'''return the dict of attributes for JSON serialization'''


def class_to_json(obj):
    ''' return the __dict__ for JSON serialization
    Args:
        obj(object): the object
    Return:
        dict: the dictionary of attr
    '''
    return obj.__dict__
