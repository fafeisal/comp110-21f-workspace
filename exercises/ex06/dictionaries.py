"""Practice with dictionaries."""

__author__ = "730474766"


def invert(main: dict[str, str]) -> dict[str, str]:
    """Function for inverting dictionary's keys and values."""
    inverted_dictionary: dict[str, str] = {}
    for key in main:
        for second_key in inverted_dictionary:
            if second_key == main[key]:
                raise KeyError("There are repeated keys in inverted_dictionary.")
        inverted_dictionary[main[key]] = key
    return inverted_dictionary


def favorite_color(census: dict[str, str]) -> str:
    """Finds highest frequency color in a dict of fav colors."""
    # go through every color and add tallies to associated
    # color in a secondary dictionary
    totals: dict[str, int] = {}
    most: str = ""
    for key in census:
        if census[key] in totals:
            totals[census[key]] += 1
        else:
            totals[census[key]] = 1
    # store the highest tallied color in another variable
    for color in totals:
        if most == "":
            most = color
        else: 
            if totals[color] > totals[most]:
                most = color
    return most


def count(items: list[str]) -> dict[str, int]:
    """Counting frequency of items in a list."""
    frequencies: dict[str, int] = {}
    i: int = 0
    while i < len(items):
        current: str = items[i]
        # place: int = 0
        # holder: int = 0
        # while place < len(items):
        #     if current == items[place]:
        #         holder += 1
        #         items.pop(place)
        #     else:
        #         place += 1
        # frequencies[current] = holder
        if current in frequencies: 
            frequencies[current] += 1
        else:
            frequencies[current] = 1
        i += 1
    return frequencies