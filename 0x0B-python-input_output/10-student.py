#!/usr/bin/python3
'''module that defines student objects'''


class Student:
    '''defines student objects'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dict object that consist only of
        attributes in attrs
        Args:
            attrs(list): list of attributes to return
        Return:
            dict: dict of selected attributes
        '''
        if attrs is None:
            return self.__dict__
        attr_dict = dict()
        for attr in attrs:
            try:
                value = self.__dict__[attr]
            except KeyError:
                continue
            attr_dict[attr] = value
        return attr_dict
