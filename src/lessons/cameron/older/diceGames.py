"""
Author: 
Date: 
Description: 
"""

import random

EYES = 2


def rollDice(num):
    """Given the number of dice, generate a random dice roll and return the sum."""
    dots = 0
    for n in range(num):
        die = random.randint(1, 6)
        print(die, end='\t')
        dots += die
    print()
    return dots


def boxcars():
    """This function is a placeholder for where boxcars from last week would appear"""
    print("Playing Boxcars!")


def snakeEyes(num):
    """this function generates paris of random numbers to be used when playing snakeeyes"""
    """start with zero snakeeyes"""
    snake_eyes_number = 0
    """iterate num times so represent the chosen number of roles"""
    for roll in range(num):
        """calculate the numbers of times EYES occurs"""
        result = rollDice(EYES)
        """if we found EYES"""
        if result == EYES:
            print("SNAKE EYES!")
            """increment the EYES count"""
            snake_eyes_number += 1
    print()
    print("Number of snakes eyes", snake_eyes_number)


def main():
    """display main menu and manage game"""
    """loop until player says stop"""
    while True:
        print("""
        1. Play Boxcars
        2. Play Snake Eyes
        3. Roll a bunch of dice
        0. Exit
        """)
        """get players choice as an int"""
        choice = int(input("Select your choice: "))
        """now execute the corresponding function, making sure to capture number of rolls where needed"""
        if choice == 1:
            boxcars()
        elif choice == 2:
            num = int(input("Number of dice rolls: "))
            snakeEyes(num)
        elif choice == 3:
            num = int(input("Number of dice rolls: "))
            rollDice(num)
        elif choice == 0:
            """quit program"""
            break
        else:
            """entered an incorrect choise; tell player and show menu again"""
            print("Please select 0, 1, 2 or 3")
    print("Thanks for playing")


"""if we are running this program"""
if __name__ == "__main__":
    """execute main function"""
    main()
