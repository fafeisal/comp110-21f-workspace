"""List utility functions."""

__author__ = "730474766"


def all(items: list[int], number: int) -> bool:
    """Verifying iff all items in list are the chosen int."""
    i: int = 0
    store: int = 0
    while i < len(items):
        position: int = items[i]
        if position == number:
            store += 1
        i += 1
    if store == len(items):
        return True
    else:
        return False


def is_equal(first: list[int], second: list[int]) -> bool:
    """Verifying iff two lists are identical in value and index."""
    i: int = 0
    position: int = 0
    while i < len(first) and len(second):
        if first[i] == second[i]:
            position += 1
        i += 1
    if position == len(first) and len(second):
        return True
    else:
        return False


def max(items: list[int]) -> int:
    """Function to return largest vlaue from a list."""
    if len(items) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    position: int = 0
    next_item: int = 1
    while i < len(items):
        if items[next_item] > items[position]:
            items[position] = items[next_item]
        if next_item < len(items) - 1:
            next_item += 1
        i += 1
    return items[position]