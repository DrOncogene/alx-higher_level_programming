#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i, printed = 0, 0
        while i < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                printed += 1
                i += 1
            else:
                i += 1
        print("\n", end='')
        return printed
    except IndexError:
        print("\n", end='')
        return printed
