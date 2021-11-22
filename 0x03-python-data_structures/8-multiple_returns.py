#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple_string = ""
    if len(sentence) == 0:
        return 0, "None"
    else:
        for args in sentence:
            new_tuple_string += args
        length = len(new_tuple_string)
        Character = new_tuple_string[0]
    return length, Character
