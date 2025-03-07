# Author: Hogan Lin
# Date: Mar 6th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Description: Implementation of sort3 (loop-free finite sort) and bubble_sort

def swap(l, i, j):
    """
    Swap elements in list l at indices i and j.
    """
    l[i], l[j] = l[j], l[i]

def sort3(l):
    """
    Sort a list of three elements using a loop-free method.
    
    :param l: List of exactly three elements
    """
    assert len(l) == 3

    if l[0] > l[1]: swap(l, 0, 1)
    if l[1] > l[2]: swap(l, 1, 2)
    if l[0] > l[1]: swap(l, 0, 1)  # Final check to ensure sorted order

def bubble_sort(l):
    """
    Perform bubble sort on a list.
    
    :param l: List of elements to be sorted
    """
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                swap(l, j, j + 1)
                swapped = True
        if not swapped:
            break  # Optimization: Stop if no swaps occurred in a pass
