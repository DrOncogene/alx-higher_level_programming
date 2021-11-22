#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        a, b = my_list[:idx], my_list[idx + 1:]
        my_list.clear()
        my_list.extend(a)
        my_list.extend(b)
        return my_list
