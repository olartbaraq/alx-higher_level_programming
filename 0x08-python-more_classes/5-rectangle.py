#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Method to Represent a Rectangle"""
#number_of_instances = 0
#print_symbol = "#"


    def __init__(self, width=0, height=0):
        """ """
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width with value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height with value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of Rectangle"""
        return ((self.width) * (self.height))

    def perimeter(self):
        """Returns perimeter of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Format Rectangle instance so that eval(self.__repr__())
        creates a new similar instance.
        Returns: string representation to recreate object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        """Rectangle is about to be deleted"""
        print("Bye rectangle...")
        #number_of_instances -= 1
