import random

words = ["eat", "four", "seven"]

print("I am thinking of a word; can you guess it?")
while True:
    secret_word = random.choice(words)
    guesses_so_far = len(secret_word) * "_"
    while True:
        print(guesses_so_far)
        guess = input("Guess a letter: ")
        if guess in secret_word:
            for position in range(len(secret_word)):
                if secret_word[position] == guess:
                    print(f"{guess} is at {position} in {secret_word}")
                    guesses_so_far = list(guesses_so_far)
                    guesses_so_far[position] = guess
                    guesses_so_far = ''.join(guesses_so_far)
        if guesses_so_far == secret_word:
            print("You won!")
            break
     yn = input"Play again?")
     if yn == "no"
        break

print("goodbye")
