#!/usr/bin/python3
""" Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle is a geomtry inherit to Base class
    Attributes:
        id (int): id of class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor of Rectange class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ return the area of Rectangle """
        return self.__height * self.__width

    def display(self):
        """ display rectangle with char # """
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """ update the class """
        attribut = ['id', 'width', 'height', 'x', 'y']
        if args and len(args):
            for i, value in enumerate(args):
                setattr(self, attribut[i], value)
        else:
            for key, value in kwargs.items():
                if key in attribut:
                    setattr(self, key, value)

    def __str__(self):
        """ str representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def to_dictionary(self):
        """ return attribute in dict"""
        the_dict = {}
        the_dict['id'] = self.id
        the_dict['width'] = self.width
        the_dict['height'] = self.height
        the_dict['x'] = self.x
        the_dict['y'] = self.y
        return the_dict
