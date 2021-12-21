#!/usr/bin/python3
"""
defines a class with instance
"""


class BaseGeometry:
    """ defines a method and returns a value"""

    def area(self):
        """ raise an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value to be int and raise appropraite error"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ a sub class from base class baseGeometry"""

    def __init__(self, width, height):
        """ instantiation of atrributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
