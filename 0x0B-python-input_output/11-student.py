#!/usr/bin/python3
"""defining a class student"""


class Student:
    """class Student
    Attributes:
        first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Methhod retrieves dict representation of Student
        instance"""
        if attrs is not None:
            my_dict = {}
            for key in attrs:
                try:
                    my_dict[key] = self.__dict__[key]
                except KeyError:
                    pass
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Method replaces all attributes of
        Student instance"""
        self.__dict__.update(json)
