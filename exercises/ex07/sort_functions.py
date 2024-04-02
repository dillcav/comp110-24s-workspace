"""Functions that implement sorting algorithms."""

__author__ = "730499558"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx1: int = 0
    while idx1 < len(x)-1:
        idx2: int = idx1 + 1
        tempidx: int = idx2
        while idx1 >= 0:
            if x[idx1] <= x[tempidx]:
                idx1 -= 1
            else:
                temp: int = x[idx1]
                x[idx1] = x[tempidx]
                x[tempidx] = temp
                tempidx = idx1
                idx1 -= 1
        idx1 = idx2
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx1: int = 0
    while idx1 < len(x):
        idx2: int = idx1 + 1
        minidx: int = idx2
        if idx2 < len(x):
            min: int = x[idx2]
            minidx: int = idx2
        while idx2 < len(x):
            if min > x[idx2]:
                min = x[idx2]
                minidx = idx2
            idx2 += 1
        if minidx < len(x):
            if x[minidx] < x[idx1]:
                temp: int = x[idx1]
                x[idx1] = x[minidx]
                x[minidx] = temp
        idx1 += 1
    return None
    