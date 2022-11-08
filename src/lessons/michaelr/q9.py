header = ["name", "flavor1", "flavor2"]
wines = [
    ["Cabernet Franc", "orange", "vanilla"],
    ["Cabernet Sauvignon", "vanilla", "cherry"],
    ["Malbec", "orange", None],
    ["MALBEC", "cherry", None],
]

counts = {}
for wine in wines:
    name = wine[0]
    name = name.split(" ")[0].upper()
    if not name in counts:
        counts[name] = 0
    counts[name] += 1

assert wines[:1] == [['Cabernet Franc', 'orange', 'vanilla']]
assert len(wines[:1]) == 1
assert wines[:1][1:] == []  # there is no second entry, only 1 with index 0
