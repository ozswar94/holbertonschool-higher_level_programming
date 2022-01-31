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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        return self.__height * self.__width
