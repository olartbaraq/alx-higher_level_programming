#!/usr/bin/python3
"""
defines a class with instance
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a sub class from base class baseGeometry"""

    def __init__(self, width, height):
        """ instantiation of atrributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
