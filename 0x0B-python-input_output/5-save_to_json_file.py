#!/usr/bin/python3
"""
defines JSON represenation to write files
"""

import json
"""
import json module for serializing non string data types
"""


def save_to_json_file(my_obj, filename):
    """
    returns written file by json module
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (json.dump(my_obj, f))
