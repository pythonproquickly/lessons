import random

print("lets play a guessing game; start score is 100")
score = 100
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number I'm thinking of: "))
    if guess == secret_number:
        print("You won!!!!")
        print("You scored: ", score)
        break
    score = score - 10
    if guess < secret_number:
        print("You guessed too low")
    else:
        print("You guess to high")

print("goodbye")
