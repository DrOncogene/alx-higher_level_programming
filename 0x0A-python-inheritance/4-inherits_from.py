#!/usr/bin/python3
'''module that checks if an obj is an instance of a class
that inherits from a given class
'''


def inherits_from(obj, a_class):
    '''checks if obj is an instance of a class that inherits from a_class
    Args:
        obj(object): the object
        a_class(type object): class to check obj against
    Return:
        True or False
    '''
    if type(obj).__name__ == a_class.__name__:
        return False

    return issubclass(type(obj), a_class)
