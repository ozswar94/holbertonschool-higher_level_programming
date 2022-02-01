#!/usr/bin/python3
""" write file utf-8 """


def write_file(filename="", text=""):
    """open file in utf-8 and write"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
