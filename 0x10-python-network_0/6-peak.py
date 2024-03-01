#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    low = 0
    high = len(list_of_integers) - 1
    peak = 0
    while low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak element
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            peak = list_of_integers[mid]

        # Search the rising slope
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1 
        else:
            low = mid + 1

    #  If no peak found, this might not be a list with a peak
    return peak  




