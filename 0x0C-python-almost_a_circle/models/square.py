#!/usr/bin/python3
'''define square objects'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class to define square objects'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        '''string representation of a square obj'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
