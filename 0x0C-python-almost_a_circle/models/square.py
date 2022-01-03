#!/usr/bin/python3
""" Defines a class Square that inherits from rectangle"""

from models.base import Base
from models.rectangle import Rectangle
""" this line imports the class Rectangle to this script"""


class Square(Rectangle):
    """declares the sub class square from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ class instantiation of the instance created with attributes"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns an informal representation of the class instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    @property
    def size(self):
        """getter method for size"""
        return self.__width

    @size.setter
    def size(self, value):
        """setter method for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ method that assigns attributes to *args and **kwargs"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError("value must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """method returns the dictionary representation of a Square"""
        dict_rep = {"id":self.id, "size":self.size, "x":self.x, "y":self.y}
        return dict_rep
