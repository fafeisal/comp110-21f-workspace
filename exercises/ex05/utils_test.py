"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730474766"


def test_only_evens_empty() -> None:
    """Testing only_evens for an empty list."""
    assert only_evens([]) == []


def test_only_evens_zero() -> None:
    """Testing only_evens for a list of only 0."""
    assert only_evens([0]) == []


def test_only_evens_many_items() -> None:
    """Testing only_evens for a list of any numbers."""
    xs: list[int] = [5, 12, 0]
    assert only_evens(xs) == [12]


def test_only_evens_other_items() -> None:
    """Testing only_evens again with different list."""
    xs: list[int] = [-2, 7, 9, 1, 0, 10]
    assert only_evens(xs) == [-2, 10]


def test_sub_empty() -> None:
    """Testing sub for an empty list."""
    xs: list[int] = []
    assert sub(xs, 3, 10) == []


def test_sub_weird_index() -> None:
    """Testing sub with a negative start and end greater than length of list."""
    xs: list[int] = [10, 30]
    assert sub(xs, -3, 10) == [10, 30]


def test_weird_start() -> None:
    """Testing sub for a start greater than length of list."""
    xs: list[int] = [10, 3, 4]
    assert sub(xs, 5, 2) == []


def test_weird_end() -> None:
    """Testing sub for an end that is below 0."""
    xs: list[int] = [10, 3, 4]
    assert sub(xs, 0, -1) == []


def test_sub_many_items() -> None:
    """Testing sub for a list of many values."""
    xs: list[int] = [5, 12, 0]
    assert sub(xs, 1, 3) == [12, 0]


def test_sub_other_items() -> None:
    """Testing sub for another list of many values."""
    xs: list[int] = [1, 2, 3, 3, 4, 0, 2]
    assert sub(xs, 0, 7) == [1, 2, 3, 3, 4, 0, 2]


def test_concat_double_empty() -> None:
    """Testing concat for two empty entries."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_one_empty() -> None:
    """Testing concat for one empty list entry."""
    xs: list[int] = [2, 4, 10]
    ys: list[int] = []
    assert concat(xs, ys) == [2, 4, 10]


def test_concat_many_items() -> None:
    "Testing concat for two lists of many entries."
    xs: list[int] = [5, 12, 0]
    ys: list[int] = [7, 9, 10]
    assert concat(xs, ys) == [5, 12, 0, 7, 9, 10]


def test_concat_other_items() -> None:
    "Testing concat again for two lists of other items."
    xs: list[int] = [4, 5, 6]
    ys: list[int] = [3, 2, 1]
    assert concat(xs, ys) == [4, 5, 6, 3, 2, 1]