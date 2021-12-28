#!/usr/bin/python3
'''module that defines a base shapes class'''
import json


class Base:
    '''defines a base shapes class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        '''returns a json string of list_dict'''
        if list_dict is None or len(list_dict) == 0:
            return "[]"
        return json.dumps(list_dict)
