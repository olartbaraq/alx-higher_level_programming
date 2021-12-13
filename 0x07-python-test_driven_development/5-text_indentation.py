#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one \
function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." \
followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    count = 0
    for i in text:
        if count == 0:
            if i == chr(32):
                continue
            else:
                count = 1
        if count == 1:
            if i is chr(63) or i is chr(58) \
               or i is chr(46):
                print(i)
                print()
                count = 0
            else:
                print("{}".format(i), end="")
