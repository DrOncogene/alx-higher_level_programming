#!/usr/bin/python3
'''appends arguments to a list and save it into a JSON file'''
import sys
from os.path import exists


save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

if not exists("add_item.json"):
    with open("add_item.json", "x"):
        pass
    save([], "add_item.json")

my_list = load("add_item.json")
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save(my_list, "add_item.json")
