#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for nb in my_list:
        if not isinstance(nb, int):
            return
    my_list.reverse()
    for nb in my_list:
        print("{:d}".format(nb))
