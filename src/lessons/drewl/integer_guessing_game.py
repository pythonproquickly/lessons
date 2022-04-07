# 2/15/2022
# Write a program in which the computer randomly chooses a number between 1 and 100.
# The player then tries to guess the number. The player starts with a score of 100.
# Every time the player guesses incorrectly, give a clue, and reduce the score by 10.
# When the player guesses correctly, display a message and show the score. The game finishes.
# Extra credit (more difficult)
# Allow the player to chose to play the game again.
# Keep the total score for all games played for the player.
# Maintain a highest score ever, by player name.

# from random import randint
# ???Do I need to import a different random function here???
import random


def show_score():
    print(f"\nPlayer score = {player_score}")


def show_game_tally():
    print(f"Total games played: {game_tally}")


game_tally = 0
rules = """\nWelcome to the integer guessing game. Guess a randomly generated number between 1 and 100. 
Incorrect answers cost 10 points."""

print(f"{rules}")
while True:
    random_number = random.randint(1, 100)
    player_score = 100
    show_game_tally()
    game_tally += 1
    # print(f"random number: {random_number}")
    while player_score >= 10:
        show_score()
        guess = int(input("Guess an integer between 1 and 100: "))
        if guess == random_number:
            print("That's correct, you win!")
            print(f"Your final score is: {player_score}. ")
            break

        player_score -= 10

        if guess < random_number:
            print("Incorrect. Your guess was below the random number.")

        elif guess > random_number:
            print("Incorrect. Your guess was above the random number.")

    print("\nGame over!")
    ask = input("Do you want to play again (y/n)? ").lower()
    if ask in ("n", "no"):
        print("Goodbye.")
        break
    print("Restarting the game.\n")


def main():
    setup_new_game()
    guess_a_number()
    is_guess_correct()
    can_play_again()


if __name__ == "__main__":
    main()
