"""EX 04 - list Utility functions practice assignment!"""

__author__ = "730499558"

def all(nums: list[int], check: int) -> bool:
    """Is every number in the list equal to the given integer?"""
    empty: list[int] = []
    if nums == empty:
        return False
    else:
        for entry in nums:
            if entry != check:
                return False
        return True
    
def max(input: list[int]) -> int:
    """What is the biggest number in the list?"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    final: int = input[0]
    index: int = 1
    while index < len(input):
        if final <= input[index]:
            final = input[index]
        index += 1
    return final

def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Are these two lists identical?"""
    if len(input1) != len(input2):
        return False
    index: int = 0
    while index < len(input1):
        if input1[index] != input2[index]:
            return False
        index += 1
    return True

def extend(input1: list[int], input2: list[int]) -> None:
    """Attach List 2 to the end of List 1!"""
    index = 0
    while index < len(input2):
        input1.append(input2[index])
        index += 1
    return None