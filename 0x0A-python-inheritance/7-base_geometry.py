#!/usr/bin/python3
""" Class BaseGeometry """


class BaseGeometry:
    def area(self):
        """  Area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  Valide integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(str(name)))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))
