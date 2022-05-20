import random

print("Welcome to the number guessing game")
highest_score = 0

while True:
    print("I am thinking of a number between 1 and 100")
    print("Can you guess it?")
    score = 100
    secret_number = random.randint(1, 100)
    while True:
        number = int(input("Enter your guess: "))
        if number == secret_number:
            print(f"You won! - your final score is {score}")
            if score > highest_score:
                highest_score = score
                print("You scored highest!!!")
            break
        score = score - 10
        print(f"Your current score: {score}")
        if number < secret_number:
            print("You guessed too low")
        else:
            print("You guessed too high")

    again = input("Play again (y/n)?: ")
    again = again.lower()
    if again == "y":
        continue
    break

print("Game over")
