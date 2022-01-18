#!/usr/bin/python3

" A class Square define "


class Square:
    """
    Square class

    Attributes:
        size (int): size of the square, private attribute
    """
    def __init__(self, size=0):
        """
            the __init__ method

            Args:
                size (int): set size in constructor
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ area return area of square """
    def area(self):
        return self.__size * self.__size

    """ my_print method print square with # """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
