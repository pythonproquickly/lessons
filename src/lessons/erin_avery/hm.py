import random

secret_number = random.randint(1, 100)

print("Can you guess the secret number?")

while True:
    guess = int(input("Your guess: "))
    if guess == secret_number:
        print("You won!")
        break
    if guess < secret_number:
        print("you guessed too low")
    else:
        print("you guess too high")

print("Goodbye")
