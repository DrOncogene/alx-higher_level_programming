#!/usr/bin/python3
'''module that checks if an obj is exactly an instance of a given class'''


def is_same_class(obj, a_class):
    '''checks if obj is exactly an instance of a_class
    Args:
        obj(object): the object
        a_class(type object): class to check obj against
    Return:
        True or False
    '''
    return (type(obj).__name__ == a_class.__name__)
