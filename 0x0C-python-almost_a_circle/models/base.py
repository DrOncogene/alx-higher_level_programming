#!/usr/bin/python3
'''module that defines a base shapes class'''
import json
import os
import csv


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
        '''retrieves a list of object dicts from json_string'''
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save a json str of list_objs to a file'''
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(Base.to_json_string([]))
                return
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

    @classmethod
    def load_from_file(cls) -> list:
        '''returns a list of instances after loading them from a json file'''
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r") as f:
            obj_list = Base.from_json_string(f.read())
            for obj in obj_list:
                list_objs.append(cls.create(**obj))

        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save an object to a file in csv format using the csv module'''
        filename = f"{cls.__name__}.csv"
        with open(filename, "w") as csvfile:
            if cls.__name__ == "Rectangle":
                attr_list = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                attr_list = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(csvfile, fieldnames=attr_list)
            csv_writer.writeheader()
            if list_objs is None or len(list_objs) == 0:
                csv_writer.writerow({})
                return
            obj_list = [obj.to_dictionary() for obj in list_objs]
            for obj in obj_list:
                csv_writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls) -> list:
        '''returns a list of objects recreated from a csv file'''
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r") as f:
            objs = csv.DictReader(f)
            for obj in objs:
                for attr, value in obj.items():
                    obj[attr] = int(value)
                list_objs.append(cls.create(**obj))

        return list_objs

# alternate forms of the above two funcs implemented
# without using the csv module
#    @classmethod
#    def save_to_file_csv(cls, list_objs):
#        '''save an object to a file in csv format'''
#        filename = f"{cls.__name__}.csv"
#        with open(filename, "w") as f:
#            if list_objs is None or len(list_objs) == 0:
#                f.write('')
#                return
#            obj_list = [obj.to_dictionary() for obj in list_objs]
#            for obj in obj_list:
#                obj_str = ''
#                if cls.__name__ == "Square":
#                    obj_str += f"{obj['id']},{obj['size']},"
#                elif cls.__name__ == "Rectangle":
#                    obj_str += f"{obj['id']},{obj['width']},{obj['height']},"
#                obj_str += f"{obj['x']},{obj['y']}\n"
#                f.write(obj_str)

#    @classmethod
#    def load_from_file_csv(cls) -> list:
#        '''returns a list of objects recreated from a csv file'''
#        filename = f"{cls.__name__}.csv"
#        if not os.path.exists(filename):
#            return []

#        list_objs = []
#        with open(filename, "r") as f:
#            content = f.readlines()
#            for line in content:
#                obj = {}
#                attr_list = line.split(',')
#                obj['id'] = int(attr_list[0])
#                obj['x'], obj['y'] = int(attr_list[-2]), int(attr_list[-1])
#               if cls.__name__ == "Rectangle":
#                   obj['width'] = int(attr_list[1])
#                   obj['height'] = int(attr_list[2])
#                elif cls.__name__ == "Square":
#                    obj['size'] = int(attr_list[1])
#
#               list_objs.append(cls.create(**obj))
#       return list_objs
