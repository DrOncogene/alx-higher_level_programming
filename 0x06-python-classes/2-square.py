#!/usr/bin/python3
'''A module that defines and manipulates square objects'''


class Square:
    '''Defines a square '''

    def __init__(self: object, size=0) -> object:
        '''The class constructor
        Args:
            size: the size of the square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
