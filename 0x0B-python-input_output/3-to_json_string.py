#!/usr/bin/python3
""" imports json module to represent to string"""
import json

"""
defines JSON represenation to string
"""


def to_json_string(my_obj):
    """
    returns the JSON represenation of an
    object to string
    """
    return (json.dumps(my_obj, sort_keys=True))
