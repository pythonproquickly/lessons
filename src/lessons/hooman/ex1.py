external_data = {
    'fred': {'fav_colr': "red", 'age': 23},
    'andy': {'fav_colr': "blue", 'age': 56},
    'sue': {'fav_colr': "green", 'age': 12},
    'bill': {'fav_colr': "xxx", 'age': 56},
}

# printing for visibility. This will be written to a file
print('name,color,age')
for name, row in external_data.items():
    flat = name
    for _, item in row.items():
        flat = flat + "," + str(item)
    print(flat)
    flat = ""
