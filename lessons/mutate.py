"""Mutating functions."""

__author__ = "730499558"


def manual_append(a: list[int], b: int):
    """Adds the integer to the end of the list!"""
    a.append(b)


def double(c: list[int]):
    """Doubles every value in the list!"""
    doubleindex: int = 0
    while doubleindex < len(c):
        c[doubleindex] *= 2
        doubleindex += 1