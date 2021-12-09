#!/usr/bin/python3
'''A module that defines and manipulates square objects'''


class Square:
    '''Defines a square '''

    def __init__(self: object, size=0, position=(0, 0)) -> object:
        '''The class constructor
        Args:
            size(int): the size of the square
        '''
        self.size = size
        self.position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''property to set the position of the square
        Args:
            none
        Return:
            int: position of the square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Calculates the area of the square
        Args:
            none
        Return:
            int: area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''prints the square with #'''
        if self.__size == 0:
            print("\n", end='')
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("\n", end='')
