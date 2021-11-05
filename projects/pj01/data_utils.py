"""Utility functions."""

__author__ = "730474766"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Display column-based table with only the first nth values per column."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        store: list[str] = []
        if rows > len(column_table[column]):
            rows = len(column_table[column])
        for i in range(0, rows):
            store.append(column_table[column][i])
        result[column] = store

    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Select columns of interest from masterlist of many."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        store: list[str] = []
        if column in names:
            for value in column_table[column]:
                store.append(value)
            result[column] = store

    return result


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine separate column-based table into a single table."""
    result: dict[str, list[str]] = {}

    for column in first_table:
        result[column] = first_table[column]
    
    for column in second_table:
        if column in result:
            result[column] += second_table[column]
        else:
            result[column] = second_table[column]

    return result


def count(items: list[str]) -> dict[str, int]:
    """Note frequencies of specific items in list."""
    result: dict[str, int] = {}

    for value in items:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1

    return result


def binary(answers: list[str]) -> dict[str, int]:
    """Frequencies of overall yes and no answers."""
    result: dict[str, int] = {}

    for value in answers:
        if value == "No":
            if value in result:
                result[value] += 1
            else:
                result[value] = 1
        else:
            if 'Yes' in result:
                result['Yes'] += 1
            else:
                result['Yes'] = 1

    return result