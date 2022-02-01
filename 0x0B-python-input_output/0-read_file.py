#!/usr/bin/python3
""" open file utf-8 """


def read_file(filename=""):
    """open file in utf-8 and print"""
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end="")
