#!/usr/bin/python3
def complex_delete(a_dict, value):
    new_dict = {}
    for k, v in a_dict.items():
        if v == value:
            new_dict[k] = v
    for k, v in new_dict.items():
        del a_dict[k]
    return a_dict
