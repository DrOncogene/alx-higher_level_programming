#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [check(x, search, replace) for x in my_list]


def check(elem, search, replace):
    if elem == search:
        return replace
    return elem
