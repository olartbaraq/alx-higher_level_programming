#!/usr/bin/python3
""" imports json module to represent to string"""
import json

"""
defines JSON represenation to string
"""


def from_json_string(my_str):
    """
    returns the JSON represenation of an
    object to string in python data structure
    """
    return (json.loads(my_str))
