#!/usr/bin/python3

" A class Square define "


class Square:
    """
    Square class

    Attributes:
        size (int): size of the square, private attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """
            the __init__ method

            Args:
                size (int): set size in constructor
                position (tuple): set position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
            isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """ area return area of square """
    def area(self):
        return self.__size * self.__size

    """ my_print method print square with # """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
