#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """Creates of the Square
    Attributes:
    __size (int): side of the square for computation
    """
    def __init__(self, size):
        """Instantiaze a Square
        Args:
            size (int): size of a side of the square
            Returns: None
            """
        self.__size = size
