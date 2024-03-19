"""EX 06 - Using Unit Tests on EX 05!"""


__author__ = "730499558"


from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
import pytest


def test_invert_use1() -> None:
    """Swapping a basic dict!"""
    test: dict[str, str] = {"A": "1", "B": "2", "C": "3"}
    assert invert(test) == {"1": "A", "2": "B", "3": "C"}


def test_invert_use2() -> None:
    """Entering a dataset with identical values!"""
    with pytest.raises(KeyError):
        test = {"A": "1", "B": "1"}
        invert(test)


def test_invert_edge() -> None:
    """Submitting a dict that already has identical keys!"""
    test: dict[str, str] = {"A": "1", "A": "1"}
    assert invert(test) == {"2": "A"}


def test_count_use1() -> None:
    """A list with no repeats!"""
    test: list[str] = ["A", "B", "C"]
    assert count(test) == {"A": 1, "B": 1, "C": 1}


def test_count_use2() -> None:
    """A list with repeats!"""
    test: list[str] = ["A", "B", "A", "B"]
    assert count(test) == {"A": 2, "B": 2}


def test_count_edge() -> None:
    """A list with capitalization differences!"""
    test: list[str] = ["A", "a", "B"]
    assert count(test) == {"A": 1, "a": 1, "B": 1}


def test_fav_color_use1() -> None:
    """Inputting a list with a majority color!"""
    test: dict[str, str] = {"A": "Yellow", "B": "Yellow", "C": "Green"}
    assert favorite_color(test) == "Yellow"


def test_fav_color_use2() -> None:
    """Inputting a list with a tied color!"""
    test: dict[str, str] = {"A": "Yellow", "B": "Blue", "C": "Green"}
    assert favorite_color(test) == "Yellow"


def test_fav_color_edge() -> None:
    """Inputting a list with someone voting twice!"""
    test: dict[str, str] = {"A": "Yellow", "A": "Yellow", "B": "Green", "C": "Green"}
    assert favorite_color(test) == "Green"


def test_alpha_use1() -> None:
    """Inputting a list with different starting letters!"""
    test: list[str] = ["Cat", "dog"]
    assert alphabetizer(test) == {"c": ["Cat"], "d": ["dog"]}


def test_alpha_use2() -> None:
    """Inputting a list with matching starting letters!"""
    test: list[str] = ["Cat", "dog", "cow"]
    assert alphabetizer(test) == {"c": ["Cat", "cow"], "d": ["dog"]}


def test_alpha_edge() -> None:
    """Inputting a list with a space in front of a value!"""
    test: list[str] = [" Cat", "dog"]
    assert alphabetizer(test) == {" ": [" Cat"], "d": ["dog"]}


def test_attend_use1() -> None:
    """Adding a new name!"""
    test: dict[str, list[str]] = {"Monday": ["Dillon"], "Tuesday": ["David"]}
    update_attendance(test, "Monday", "Mack")
    assert test == {"Monday": ["Dillon", "Mack"], "Tuesday": ["David"]}


def test_attend_use2() -> None:
    """Adding an existing name!"""
    test: dict[str, list[str]] = {"Monday": ["Dillon"], "Tuesday": ["David"]}
    update_attendance(test, "Monday", "Dillon")
    assert test == {"Monday": ["Dillon"], "Tuesday": ["David"]}


def test_attend_edge() -> None:
    """Adding a made up day!"""
    test: dict[str, list[str]] = {"Monday": ["Dillon"], "Tuesday": ["David"]}
    update_attendance(test, "Ice Cream", "Mack")
    assert test == {"Monday": ["Dillon"], "Tuesday": ["David"], "Ice Cream": ["Mack"]}