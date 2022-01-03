#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for nb in my_list:
        if type(0) == type(nb):
            print("{:d}".format(nb))
