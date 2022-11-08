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

assert counts == {'CABERNET': 2, 'MALBEC': 2}

assert len(counts) == 2  # two key value pairs in dict
