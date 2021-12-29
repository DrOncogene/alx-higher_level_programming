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
    def to_json_string(list_dict) -> str:
        '''returns a json string of list_dict
        Args:
            list_dict(list): a list of dictionaries
        Return:
            str: json string
        '''
        if list_dict is None or len(list_dict) == 0:
            return "[]"
        return json.dumps(list_dict)

    @staticmethod
    def from_json_string(json_string) -> list:
        '''retrieves a list of objects from json_string'''
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save a json str of list_objs to a file'''
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary) -> object:
        '''creates an object from attributes in dictionary'''
        if cls.__name__ == "Rectangle":
            new = cls(2, 2)
        elif cls.__name__ == "Square":
            new = cls(2)
        new.update(**dictionary)

        return new
