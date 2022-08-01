import string
import random

password_characters = string.ascii_letters+string.digits+string.punctuation
password_length = random.randint(8,12)
password = ""

for i in range(password_length):
    password+=random.choice(password_characters)

print(password)