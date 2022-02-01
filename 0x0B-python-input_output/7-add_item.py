#!/usr/bin/python3
""" add item """
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    obj = load_from_json_file("add_item.json")
except:
    obj = []

if len(sys.argv) > 1:
    for i in range(1, sys.argc):
        obj.append(argv[i])

save_to_json_file(obj, "add_item.json")
