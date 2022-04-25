cities = {
    "London": {"continent": "Europe", "population": "9 million", "language": "English"},
    "Paris": {"continent": "Europe", "population": "2.2 million", "language": "French"},
    "Melbourne": {"continent": "Oceana", "population": "5 million", "language": "English"},
}
"""# Print info on all 3 cities using a fstring
for city, info in cities.items():
    print(f"Here's some information about {city}: It is in {info['continent']}, "
          f"it has a population of roughly {info['population']} and the official language there is {info['language']}.")
for city, info in cities.items():
    # creates a list of all the cities by appending all the keys of the dictionaries into a list
    list_of_cities = []
    list_of_cities.append(city)
    # Asks the user for his/ her favorite city
    favorite_city = input("What is your favorite city?")
    # If the input corresponds to one ot the cities in the dictionary, information on the city is printed
    if favorite_city in list_of_cities:
        print(f"{cities[favorite_city]}")  # In this line, I see that I can access
        # the nested dictionary using "cities[favorite_city]
        for city, info in cities[favorite_city].items(): # The items function doesn't work here
    # I would like to access the embedded dictionary with the key that corresponds to the input given by the user
    # (the value in favorite_cities) so that if the user prints "Paris" for example, information on Paris is given.
    elif favorite_city not in list_of_cities:  # Python says there is an indentation error here as well.
        print(f"Sorry, {favorite_city} is not in our database.")"""

while True:
    your_favorite_city = input("What is your favorite city?: ")
    if your_favorite_city not in cities:
        print("That can't be a favorite city")
        continue
    break
print(f"Your favorite city is {your_favorite_city}")
