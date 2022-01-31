#!/usr/bin/python3
"""Inherits from a list"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """print list sorted"""
        print(sorted(self))
