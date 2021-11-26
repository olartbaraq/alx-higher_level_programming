#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    ints = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i in range(len(roman_string)):
        value = ints[roman_string[i]]
        if i+1 < len(roman_string) and ints[roman_string[i+1]] > value:
            result -= value
        else:
            result += value
    return result
