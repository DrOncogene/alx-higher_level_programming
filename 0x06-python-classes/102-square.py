#!/usr/bin/python3
'''A module that defines and manipulates square objects'''


class Square:
    '''Defines a square '''

    def __init__(self: object, size=0) -> object:
        '''The class constructor
        Args:
            size(int): the size of the square
        '''
        self.size = size

    def area(self):
        '''Calculates the area of the square
        Args:
            none
        Return:
            int: area of the square
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''size getter
        Args:
            none
        Return:
            int: size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter
        Args:
            value(int): the size
        Return:
            int: size of the square
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, square2):
        '''< operator overload'''
        return self.area() < square2.area()

    def __gt__(self, square2):
        '''> operator overload'''
        return self.area() > square2.area()

    def __eq__(self, square2):
        '''== operator overload'''
        return self.area() > square2.area()

    def __le__(self, square2):
        '''<= operator overload'''
        return self.area() <= square2.area()

    def __ge__(self, square2):
        '''>= operator overload'''
        return self.area() >= square2.area()

    def __ne__(self, square2):
        '''!= operator overload'''
        return self.area() != square2.area()
