#!/usr/bin/python3
'''A module that defines and manipulates square objects'''


class Square:
    '''Defines a square '''

    def __init__(self: object, size: int) -> object:
        '''The class constructor
        Args:
            size: the size of the square
        '''
        self.__size = size
