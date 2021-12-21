#!/usr/bin/python3
""" class inherited directly or indirectly"""


def inherits_from(obj, a_class):
    """returns True if object is an instance"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
