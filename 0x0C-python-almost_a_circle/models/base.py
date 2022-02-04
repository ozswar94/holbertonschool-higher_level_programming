#!/usr/bin/python3
""" Base class """


class Base:
    """
    class Base is a geomtry class base
    Attributes:
        id (int): number of instance
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """ constructor of Base class """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
