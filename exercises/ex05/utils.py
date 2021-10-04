"""List utility functions part 2."""

__author__ = "730474766"


def only_evens(values: list[int]) -> list[int]:
    """Function to return only the evens in a list."""
    i: int = 0
    while i < len(values):
        if values[i] == 0:
            values.pop(i)
        else: 
            if (values[i] % 2) != 0:
                values.pop(i)
            else:
                i += 1
    return values


def sub(values: list[int], start: int, end: int) -> list[int]:
    """Function for printing list of ints from start to end index."""
    if start < 0:
        start = 0
    if end > len(values):
        end = len(values)
    i: int = start
    output: list[int] = []
    # if (len(values) == 0) or (start > len(values)) or (end <= 0):
    #     return output
    while i < (end):
        output.append(values[i])
        i += 1
    return output


def concat(one: list[int], two: list[int]) -> list[int]:
    """Function two combine both input lists."""
    i: int = 0
    new: list[int] = []
    while i < len(one):
        new.append(one[i])
        i += 1
    i = 0
    while i < len(two):
        new.append(two[i])
        i += 1
    return new