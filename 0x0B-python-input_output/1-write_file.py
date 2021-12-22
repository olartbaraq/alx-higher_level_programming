#!/usr/bin/python3
"""
contains the write-file function
"""


def write_file(filename="", text=""):
    """
    writes a text file(UTF8) and returns
    number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
