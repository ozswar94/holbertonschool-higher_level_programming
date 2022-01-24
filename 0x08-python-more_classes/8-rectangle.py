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

        number_of_instances (int): counter of
        instannce Rectangle

        print_symbol (str): a symbole print when we print rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        __init__ method is the constructor of the class Rectangle

        Args:
            width (int): set width in constructor
            height (int): set height in constructor
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal
        the biggest rectangle based on the area

        Args:
            rect_1: the first rectangle compare
            rect_2: the seconde rectangle compare
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2

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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    """ return area of rectange """
    def area(self):
        return self.__width * self.__height

    """ return perimeter of rectangle """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    """ return the string rectangle with the char = '#' """
    def __str__(self):
        rect = ""
        for i in range(self.__height):
            for j in range(self.width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += '\n'
        return rect

    """ return the representation of Rectangle """
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    """ destructor of class Rectangle """
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
