#!/usr/bin/python3
'''module that defines geometric shapes'''


class BaseGeometry:
    '''defines geometric shape objects'''
    def area(self):
        '''raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value as an integer > 0
        Args:
            name(str): name of a shape
            value(int): integer value
        Return:
            nothing
        '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
