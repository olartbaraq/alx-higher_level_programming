#!/usr/bin/python3
"""
defines a class with instance
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a subclass that inheritis from class Rectangle"""

    def __init__(self, size):
        """instantiation of attributes"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size) ** 2

    def __str__(self):
        """string representation of object"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
