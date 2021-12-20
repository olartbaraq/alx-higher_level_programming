#!/usr/bin/python3
"""
function that returns list of avaiable attributes \
and method of an object
"""


def lookup(obj):
    """returns a list of methods and atrributes"""
    return (dir(obj))
