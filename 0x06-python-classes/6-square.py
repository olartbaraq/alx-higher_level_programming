#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """Represents a Square with its size
    Attributes:
    __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): the cordinate position of the sqaure on the plane
        Returns:
            None
        """
        self.size = size
        self.position = position

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
         Return:
              None
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def position(self):
        """ getter method for position
        Returns:
            The position of the square
        """
        return self.__position

    def position(self, value):
        """ setter method for position
        Args:
             value (tuple): the position of the size of the square
        Returns:
             None
        """
        if type(value) is not tuple or \
           len(value) != 2 or \
           any(map(lambda x: type(x) is not int or x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints in standard output
          Square with character # at a position"
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
