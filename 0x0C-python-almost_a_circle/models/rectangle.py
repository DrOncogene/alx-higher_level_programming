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
        return self.__y

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

    def display(self):
        '''displays the rectangle using #'''
        for i in range(self.y):
            print('')
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print('')

    def __str__(self):
        '''string representation of a rect obj'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''assigns new values to the rect attributes using *args'''
        attr_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0:
            if len(args) <= len(attr_list):
                attr_list = attr_list[:len(args)]
            for i in range(len(attr_list)):
                self.__update_attr(i, args[i])
            return

        attr_list = ["id", "width", "height", "x", "y"]
        for key, value in kwargs.items():
            try:
                index = attr_list.index(key)
            except ValueError:
                continue
            self.__update_attr(index, value)

    def __update_attr(self, index, value):
        '''convinience method to set attrs from within update() method'''
        if index == 0:
            self.id = value
        elif index == 1:
            self.width = value
        elif index == 2:
            self.height = value
        elif index == 3:
            self.x = value
        elif index == 4:
            self.y = value

    def to_dictionary(self) -> dict:
        '''returns a dict of the rect object attributes'''
        attr_dict = {}
        attr_dict['x'] = self.x
        attr_dict['y'] = self.y
        attr_dict['id'] = self.id
        attr_dict['height'] = self.height
        attr_dict['width'] = self.width
        return attr_dict
