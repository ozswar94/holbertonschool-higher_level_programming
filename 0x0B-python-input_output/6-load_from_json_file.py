#!/usr/bin/python3
""" json file to object """


import json


def load_from_json_file(filename):
    """file to json object"""
    with open(filename, 'r') as f:
        return json.load(f)
