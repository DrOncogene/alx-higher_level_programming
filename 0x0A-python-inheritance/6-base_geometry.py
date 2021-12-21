#!/usr/bin/python3
'''module that defines geometric shapes'''


class BaseGeometry:
    '''defines geometric shape objects'''
    def area(self):
        '''raises an exception'''
        raise Exception("area() is not implemented")
