#!/usr/bin/python3
""" instance of an object or class"""


def is_kind_of_class(obj, a_class):
    """ returns bool true if object is an instance """
    if isinstance(obj, a_class):
        return True
    else:
        return False
