#!/usr/bin/python3
"""
Defines a class """


class Student():
    """Defines a class with attributes"""

    def __init__(self, first_name, last_name, age):
        """ instantiation of certain attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method to retrieve a dictionary representation"""
        return self.__dict__
