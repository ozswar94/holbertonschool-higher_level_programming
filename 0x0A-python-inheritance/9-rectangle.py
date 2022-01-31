#!/usr/bin/python3
""" Class Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle

    Attributes:
        width (int): width of Rectangle
        height (int): height of Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """ return area of rectangle """
        return self.__height * self.__width
