#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for nb in my_list:
        if not isinstance(nb, int):
            return
    for nb in my_list:
        print("{:d}".format(nb))
