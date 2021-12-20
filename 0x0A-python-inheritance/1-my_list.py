#!/usr/bin/python3
"""
Mylist inheritace
"""


class MyList(list):
    """a subclass of class list"""
    def print_sorted(self):
        """prints the soreted list """
        print(sorted(self))
