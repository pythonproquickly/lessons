records = [
    ["john", 10075],
    ["paul", 10067],
    ["george", 10082],
    ["ringo", 10051],
]
lowest = float("inf")
name = ""
for record in records:
    if record[1] < lowest:
        lowest = record[1]
        name = record[0]
actual_lowest = lowest
lowest = float("inf")
for record in records:
    if record[1] == actual_lowest:
        continue
    if record[1] < lowest:
        lowest = record[1]
        name = record[0]
print(name, lowest)
