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


class Rectangle(BaseGeometry):
    '''defines rectangle shape objects'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''returns the area of the rectangle
        Args:
            none
        Return:
            int: area of the rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''string representation of rectangles'''
        return f"[Rectangle {self.__width}/{self.__height}"
