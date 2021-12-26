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

    def to_json(self, attrs=None):
        """method to retrieve a dictionary representation"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
