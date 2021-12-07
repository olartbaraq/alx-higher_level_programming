#!/usr/bin/python3
"""defines a class Square"""
class Square:
    """Represents a Square with its size
    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
    def area(self):
        """Returns the value of Square Area"""
        return (self.__size) ** 2
