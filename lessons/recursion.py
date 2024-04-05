"""CQ07 - Defining a Function Recursively!"""

__author__ = "730499558"


def f(n: int, k: int) -> int:
    """Recursive version of n*k!"""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return k + f(n - 1, k)