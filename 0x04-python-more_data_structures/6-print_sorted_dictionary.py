#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary)
    for i in sort:
        print("{:s}: {}".format(i, a_dictionary[i]))
