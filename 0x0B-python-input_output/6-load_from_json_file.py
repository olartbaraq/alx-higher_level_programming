#!/usr/bin/python3
"""
Defines an object using JSON file
"""

import json
"""
imports the module json for function usage
"""


def load_from_json_file(filename):
    """
    function that creates an object from json file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return (json.load(f))
