#!/usr/bin/python3
""" Student """


class Student:
    """
    Class Student

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """
    def __init__(self, first_name, last_name, age):
        """constructor of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return class in format dictionary"""
        return self.__dict__
