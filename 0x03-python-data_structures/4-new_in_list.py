#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list) - 1:
        return my_list.copy()
    elif idx > 0 and idx < len(my_list):
        for i in range(len(my_list)):
            copy[idx] = element
            return copy