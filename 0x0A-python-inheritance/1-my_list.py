#!/usr/bin/python3
""" My List """


class MyList(list):
    """ subclass of list """
    def print_sorted(self):
        """ print list sorted """
        print(sorted(self))
