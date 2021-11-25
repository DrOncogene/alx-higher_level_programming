#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    for k, v in sorted(a_dict.items()):
        print("{:s}: {}".format(k, v))
