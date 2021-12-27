#!/usr/bin/python3
'''module that define and manipulate rectangle objects'''
from models.base import Base


class Rectangle(Base):
    '''class for defining rect objects'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validate_input("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validate_input("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validate_input("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__width

    @y.setter
    def y(self, value):
        Rectangle.validate_input("y", value)
        self.__y = value

    def validate_input(name: str, value: int):
        '''ensures value is an int'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        '''calculates and return the area of this rect'''
        return self.width * self.height

