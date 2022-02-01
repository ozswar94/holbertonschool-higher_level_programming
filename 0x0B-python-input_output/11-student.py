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

    def to_json(self, attrs=None):
        """return class in format dictionary"""
        try:
            dict_json = {}
            for ele in attrs:
                if ele in self.__dict__:
                    dict_json[ele] = self.__dict__[ele]
            return dict_json
        except TypeError:
            return self.__dict__

    def reload_from_json(self, json):
        """modify class attributes by json"""
        for attrs in json:
            if attrs in self.__dict__:
                self.__dict__[attrs] = json[attrs]
