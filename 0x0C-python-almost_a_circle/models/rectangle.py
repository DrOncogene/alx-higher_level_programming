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
        if len(args) <= len(self.__dict__):
            attr_list = list(self.__dict__)[:len(args)]
        else:
            attr_list = list(self.__dict__)

        for i in range(len(attr_list)):
            self.__dict__[attr_list[i]] = args[i]

        if args is not None and len(args) > 0:
            return

        attr_list = list(self.__dict__)
        for key, value in kwargs.items():
            if key == "id":
                self.__dict__[key] = value
            mangled = f"_Rectangle__{key}"
            if mangled in attr_list:
                self.__dict__[mangled] = value
