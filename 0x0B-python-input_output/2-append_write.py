#!/usr/bin/python3
""" append on file utf-8 """


def append_write(filename="", text=""):
    """open file in utf-8 and apppend on file"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
