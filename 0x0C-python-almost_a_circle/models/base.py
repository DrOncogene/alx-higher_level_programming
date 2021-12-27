#!/usr/bin/python3
'''module that defines a base shapes class'''


class Base:
    '''defines a base shapes class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
