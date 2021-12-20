#!/usr/bin/python3
'''module that returns a list of attr and methods available for an object'''


def lookup(obj: object) -> list:
    '''returns a list of attr and methods of obj
    Args:
        obj(object): the object
    Return:
        list: list of obj's attr and methods
    '''
    return dir(obj)
