#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{0}".format(my_list[i]), end='')
            i += 1
        print("\n", end='')
        return i
    except IndexError:
        print("\n", end='')
        return i
