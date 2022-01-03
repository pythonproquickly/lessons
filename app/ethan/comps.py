names = [name.capitalize() for name in ("andy", "sue", "pete")]
assert names == ["Andy", "Sue", "Pete"]

some_names = [name for name in names if name[0] != "S"]
assert some_names == ["Andy", "Pete"]

# noinspection PyTypeChecker
some_names.append(sum([num for num in range(0, 20, 4)]))
assert some_names == ["Andy", "Pete", 40]
