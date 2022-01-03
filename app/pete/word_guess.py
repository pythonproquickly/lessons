import random

words = ("axe", "four", "another", "fives", "zzzzzzzzzzz")
secret_word = random.choice(words)
print("I am thinking of a word; here it is:")

guesses_so_far = "_" * len(secret_word)

letters_guessed = []
my_attempt = " " * len(secret_word)
while True:
    print(guesses_so_far)
    guess = input("Guess a letter, 9 to quit: ")
    if guess == "9":
        break
    letters_guessed.append(guess)
    if guess in secret_word:
        for index_number, letter in enumerate(secret_word):
            if letter == guess:
                guesses_so_far.replace(" ", "")
                guesses_so_far = list(guesses_so_far)
                guesses_so_far[index_number] = guess
                guesses_so_far = "".join(guesses_so_far)
        my_attempt += guess
        print(f"correct letter: {my_attempt}")
    else:
        print(f"Incorrect; try again {''.join(letters_guessed)}")
    if guesses_so_far == secret_word:
        print("YOU WON")
        break
