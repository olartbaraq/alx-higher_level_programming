#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
     if list_of_integers == []:
         return None
     l = len(list_of_integers)
     m = l // 2
     arr = list_of_integers
     while True:
         if m != 0 and m != l - 1 and arr[m - 1] < arr[m] < arr[m + 1]:
             m = (l + m) // 2
         elif m != 0 and m != l - 1 and arr[m - 1] > arr[m] > arr[m + 1]:
             m = m // 2
         elif m != 0 and m != l - 1 and arr[m - 1] > arr[m] < arr[m + 1]:
             m = m // 2
         else:
             return arr[m]
                                                     
