#!/usr/bin/python3
'''module that contain a class whose objects prevent dynamic
attribute allocation'''


class LockedClass:
    '''defines an object that cannot be dynamically allocated
    new attributes'''
    def __setattr__(self, attr, value):
        if attr == 'first_name':
            self.__dict__[attr] = value
        else:
            raise AttributeError("'{}' object has no \
attribute '{}'".format(self.__class__.__name__, attr))
