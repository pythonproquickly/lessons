# Write a program in which the computer randomly chooses a number between 1 and 100. The player then tries
#  to guess the number.
# The player starts with a score of 100.
# Every time the player guesses incorrectly, give a clue, and reduce the score by 10.
# When the player guesses correctly, display a message and show the score. The game finishes.
# Extra credit (more difficult)
# Allow the player to chose to play the game again.
# Keep the total score for all games played for the player.
# Maintain a highest score ever, by player name.
import random

player_score = 100
player_guesses = 10
x = random.randint(1, 100)
print(x)
print(f"Your score is now {player_score} and you have {player_guesses} guesses left")
for guess in range(player_guesses):
    while player_score > 0:
        guess1 = int(
            input(
                "Guess a number between 1 and 100. Note: every incorrect guess subtracts 10 from your score: "
            )
        )
        if guess1 == x:
            print(
                f"You have won!! What are the odds of that?? your score is {player_score} "
            )
            break
        else:
            print("That is not the number we are looking for")
            player_score -= 10
            player_guesses -= 1
    print(f"You have {player_guesses} guesses left and your score is {player_score}")

    print(f"your score in this round: {player_score}")
    play_again = input("would you like to play again? (y/n): ")
    if play_again == "y":
        continue
    else:
        break
