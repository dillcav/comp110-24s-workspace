"""Splitting a dictionary into two lists!"""

__author__ = "730499558"


def get_keys(input: dict[str,int]) -> list[str]:
    """Provides a list of keys!"""
    answer: list[str] = []
    for key in input:
        answer.append(key)
    return answer


def get_values(input: dict[str,int]) -> list[int]:
    """Provides a list of values!"""
    answer: list[int] = []
    for key in input:
        answer.append(input[key])
    return answer