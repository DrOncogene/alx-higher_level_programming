#!/usr/bin/python3
'''module that checks if an obj is an instance of a given class
or any of its superclasses
'''


def is_kind_of_class(obj, a_class):
    '''checks if obj is an instance of a_class or its parents
    Args:
        obj(object): the object
        a_class(type object): class to check obj against
    Return:
        True or False
    '''
    return isinstance(obj, a_class)
