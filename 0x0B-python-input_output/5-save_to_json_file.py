#!/usr/bin/python3
""" write a json on file """


import json


def save_to_json_file(my_obj, filename):
    """open file in utf-8 and write the json on file"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
