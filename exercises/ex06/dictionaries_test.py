"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest

__author__ = "730474766"


# unit tests for invert
def test_invert_key_error() -> None:
    """Testing for KeyError in invert with repeat keys."""
    with pytest.raises(KeyError):
        invert({'a': 'b', 'm': 'b'})


def test_invert_empty() -> None:
    """Testing invert for an empty dictionary."""
    assert invert({}) == {}


def test_invert_use() -> None:
    """Testing invert for a simple use case."""
    assert invert({'a': 'b', 'z': 'm', 'm': 'a'}) == ({'b': 'a', 'm': 'z', 'a': 'm'})


def test_invert_second_use() -> None:
    """Testing invert for another simple use case."""
    assert invert({'sir': 'maam', 'boy': 'girl'}) == ({'maam': 'sir', 'girl': 'boy'})


# unit tests for favorite_color
def test_favorite_color_empty() -> None:
    """Testing favorite_color for an empty dictionary."""
    assert favorite_color({}) == ''


def test_favorite_color_use() -> None:
    """Testing favorite_color for a simple use case."""
    assert favorite_color({'Mary': 'blue', 'Cindy': 'green'}) == 'blue'


def test_favorite_color_second_use() -> None:
    """Testing favorite_color for a second use case."""
    assert favorite_color({'Terry': 'red', 'Maddy': 'blue', 'Cheryl': 'red', 'Amethyst': 'orange'}) == 'red'


# unit tests for count
def test_count_empty() -> None:
    """Testing count for an empty list."""
    assert count([]) == {}


def test_count_use() -> None:
    """Testing count for a simple use case."""
    assert count(['perry', 'sam', 'george']) == {'perry': 1, 'sam': 1, 'george': 1}


def test_count_second_use() -> None:
    """Testing count for a second use case."""
    assert count(['a', 'c', 'b', 'b', 'd', 'a', 'a']) == {'a': 3, 'c': 1, 'b': 2, 'd': 1}