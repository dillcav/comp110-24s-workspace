"""Test my garden functions."""

__author__ = "730499558"


from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_kind_use() -> None:
    """Testing add_by_kind with an existing kind."""
    test: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(test, "flower", "rose")
    assert test == {"flower": ["marigold", "zinnia", "rose"], "vegetable": ["carrots"]}


def test_kind_edge() -> None:
    """Testing add_by_kind where the kind and plant are swapped."""
    test: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(test, "rose", "flower")
    assert test == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "rose": ["flower"]}


def test_date_use() -> None:
    """Testing add_by_date with an existing date."""
    test: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(test, "June", "stringbeans")
    assert test == {"April": ["marigold"], "June": ["carrots", "stringbeans"]}


def test_date_edge() -> None:
    """Testing add_by_date where the full entry already exists."""
    test: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(test, "June", "carrots")
    assert test == {"April": ["marigold"], "June": ["carrots", "carrots"]}


def test_kind_date_use() -> None:
    """Testing lookup_by_kind_and_date when there is an existing entry."""
    testkind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    testdate: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(testkind, testdate, "flower", "April") == "flowers to plant in April: ['marigold']"


def test_kind_date_edge() -> None:
    """Testing lookup_by_kind_and_date when an entry is present twice in one list."""
    testkind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    testdate: dict[str, list[str]] = {"April": ["marigold", "marigold"], "June": ["carrots"]}
    assert lookup_by_kind_and_date(testkind, testdate, "flower", "April") == "flowers to plant in April: ['marigold', 'marigold']"