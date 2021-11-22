#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    else:
        return [not bool(num % 2) for num in my_list]
