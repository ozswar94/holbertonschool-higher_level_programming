#!/usr/bin/python3


" A class Square define "


class Square:
    """
    Square class

    Attributes:
        size (int): size of the square, private attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
