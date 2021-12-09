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
        self.size = size

    def area(self):
        """Returns the value of Square Area"""
        return (self.__size) ** 2

    def size(self):
        """getter method
              Returns:
               The size of the square
        """
        return self.__size

    def size(self, value):
        """setter method
               Args:
               value (int): the size of a size of the square
               Returns:
               None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints in standard output
          Square with character #
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("".join(["#" for j in range(self.size)]))
