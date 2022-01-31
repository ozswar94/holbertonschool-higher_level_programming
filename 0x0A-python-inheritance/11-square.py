#!/usr/bin/python3
""" Class Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square

    Attributes:
        size (int): size of square
    """
    def __init__(self, size):
        """ constructor square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ string representation """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """ area square """
        return self.__size ** 2
