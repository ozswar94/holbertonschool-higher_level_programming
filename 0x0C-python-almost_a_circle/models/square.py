#!/usr/bin/python3
""" Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square is a geomtry inherit to Rectangle class
    Attributes:
        id (int): id of class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ square constructor """
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the class """
        attribut = ['id', 'size', 'x', 'y']
        if args and len(args):
            for i, value in enumerate(args):
                setattr(self, attribut[i], value)
        else:
            for key, value in kwargs.items():
                if key in attribut:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return attribute in dict"""
        the_dict = {}
        the_dict['id'] = self.id
        the_dict['size'] = self.width
        the_dict['x'] = self.x
        the_dict['y'] = self.y
        return the_dict
