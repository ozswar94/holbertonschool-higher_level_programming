#!/usr/bin/python3


" A Class Square "


class Rectangle:
    """
    Rectangle Class

    Attributes:
        width (int): An integer which is >= 0,
        define the width of the Rectangle

        height (int): An integer which is >= 0,
        define the height of the Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        __init__ method is the constructor of the class Rectangle

        Args:
            width (int): set width in constructor
            height (int): set height in constructor
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ return area of rectange """
        return self.__width * self.__height

    def perimeter(self):
        """ return perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ return the string rectangle with the char = '#' """
        rect = ""
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.width):
                rect += '#'
            if i < self.__height - 1:
                rect += '\n'
        return rect
