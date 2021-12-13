#!/usr/bin/python3
"""
Defines a class Rectangle with attributes"""


class Rectangle:
    """Method to Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """ """
        self.width = width
        self.height = height

    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    def width(self, value):
        """setter for the private instance attribute width with value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    def height(self, value):
        """setter for the private instance attribute height with value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
