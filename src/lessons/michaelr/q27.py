movies = [
    {"title": "A", "year": 18, "style": "short", "genres": ["g1"]},
    {"title": "B", "year": 18, "style": "long", "genres": ["g2"]},
    {"title": "C", "year": 19, "style": "short", "genres": ["g3"]},
    {"title": "D", "year": 19, "style": "long", "genres": ["g1", "g2", "g3"]}
]

assert movies[3] == {"title": "D", "year": 19, "style": "long",
                     "genres": ["g1", "g2", "g3"]}
assert movies[3]["genres"] == ["g1", "g2", "g3"]
assert movies[1]["genres"][0] == "g2"

# g2 appears in movies[3]["genres"] at index 1 (2nd position)
assert movies[3]["genres"].index(movies[1]["genres"][0]) == 1
