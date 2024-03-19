"""EX 05 - Creating a dictionary!"""


__author__ = "730499558"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Swap the keys and values!"""
    output: dict[str, str] = dict()
    for elem in input:
        for term in output:
            if input[elem] == term:
                raise KeyError("There is a duplicate key!")
        output[input[elem]] = elem
    return output


def favorite_color(input: dict[str, str]) -> str:
    """Return the most popular color!"""
    output: dict[str, int] = dict()
    for colors in input:
        if input[colors] in output:
            output[input[colors]] += 1
        else:
            output[input[colors]] = 1
    result: int = 0
    for colors in output:
        if output[colors] > result:
            result = output[colors]
            final = colors
    return final


def count(input: list[str]) -> dict[str, int]:
    """How many times is each value in the list!"""
    output: dict[str, int] = dict()
    for elem in input:
        if elem in output:
            output[elem] += 1
        else:
            output[elem] = 1
    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Sort words into their first letter!"""
    output: dict[str, list[str]] = dict()
    for elem in input:
        if elem.lower()[0] in output:
            output[elem.lower()[0]].append(elem)
        else:
            step: list[str] = list()
            output[elem.lower()[0]] = step
            output[elem.lower()[0]].append(elem)
    return output
            

def update_attendance(input: dict[str, list[str]], day: str, name: str) -> None:
    """Add names to the attendance sheet!"""
    if day in input:
        if name not in input[day]:
            input[day].append(name)
    else:
        step: list[str] = list()
        input[day] = step
        input[day].append(name)
    return None