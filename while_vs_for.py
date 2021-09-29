xs: list[str] = ["a", "b", "c"]
i: int = 0

while i < len(xs):
    item: str = xs[i]
    print(item)
    i += 1

for item in xs:
    print(item)