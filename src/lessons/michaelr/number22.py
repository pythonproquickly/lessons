airbnb = [
    {"name": "A", "room_id": 837, "start_year": 2021, "reviews": [""]},
    {"name": "B", "room_id": 389, "start_year": 2021,
     "reviews": ["*", "", "**"]},
    {"name": "C", "room_id": 108, "start_year": 2021,
     "reviews": ["***", "**"]},
    {"name": "D", "room_id": 237, "start_year": 2020, "reviews": ["*"]},
    {"name": "E", "room_id": 278, "start_year": 2020,
     "reviews": ["***", "**", "***"]},
]

counts = {}
for item in airbnb:
    reviews = item["reviews"]
    for review in reviews:
        if review not in counts:
            counts[review] = 0  # should be 1 (or all counts are 1 too low)
        else:
            counts[review] += 1

print(counts)
