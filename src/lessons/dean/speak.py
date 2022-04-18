"""fred went shopping
andy went walking
dean went running"""

import random
number_of_phrases = 10

nouns = ['fred', 'andy', 'my dog', 'girls']
verbs = ['is', 'likes', 'went']
actions = ['swimming', 'drinking', 'flying', 'sleeping']

for number in range(number_of_phrases):
    print(random.choice(nouns).title() + " " + random.choice(verbs) + " " + random.choice(actions) + ".")


person = {'name': 'andy', 'age': 42}
person2 = ['andy', 42]

grammer = {('singular', 'positive'): ['like', 'enjoys']}

grammer[('singular', 'positive')]

if grammer == ('singular', 'positive'):
    words = ['like', 'enjoys']
