people = ["andy", 22, 45.12, "green"]


countries = {"us": "usa", "uk": "United Kingdom", "fr": "France"}

countries["xyz"] = 999
countries["us"] = "Uganada"

for code, country in countries.items():
    print(f"code is {code} country is {country}")

print(countries.items())



people = {
            ('andy', 'miles'): {'age': 42, 'favcol': 'green'},
            ('fred', 'blogs'): {'age': 33, 'favcol': 'red'},
}


peoples_fav_cols = {}

print(people[('andy', 'miles')])

