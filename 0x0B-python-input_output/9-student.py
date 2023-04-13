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

    def to_json(self):
        """Methhod retrieves dict representation of Student
        instance"""
        return self.__dict__
