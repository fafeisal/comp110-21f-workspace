"""Drawing forests in a loop."""

__author__ = "730474766"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
row: str = ""

if depth > 0:
    while i < depth:
        row += TREE
        print(row)
        i += 1