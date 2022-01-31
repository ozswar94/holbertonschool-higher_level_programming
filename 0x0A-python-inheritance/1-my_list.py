#!/usr/bin/python3
""" My List """


class MyList(list):
    """
    Class MyList
    """
    def print_sorted(self):
        """ print list sorted """
        print(sorted(self))
