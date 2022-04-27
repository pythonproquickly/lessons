#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:09:01 2022

@author: gshriivanth
"""
import random
import sys

WORD_LENGTH = 5
ROW_LENGTH = 5
COLUMN_LENGTH = 6
GUESSES = 6


def initialize_grid():
    row = "_ _ _ _ _"
    grid = [row for _ in range(COLUMN_LENGTH)]
    colors_grid = grid.copy()
    return grid, colors_grid


def display_grid(grid):
    for row in grid:
        print(row)


def populate_grid(word, grid, turn):
    word = list(word)
    word = ' '.join(word)
    grid[turn - 1] = word
    return grid


def change_cell_background_color(color_grid, grid, guess, word, turn):
    row = list(color_grid[turn])

    for i in range(5):
        if guess[i] == word[i]:
            row[i] = "G"
        elif guess[i] in word:
            row[i] = "Y"
    row = ''.join(row)
    color_grid[turn] = row
    return color_grid


def get_user_input():
    while True:
        word = input("Enter your guess: ")
        if len(word) != WORD_LENGTH:
            print("type letter a 5 letter word")
            continue
        return word


def check_win_or_lose(guess, word, turn):
    if guess == word:
        return True
    if turn == GUESSES:
        return False


def check_word_in_wordbank(word, word_bank):
    return word in word_bank


def check_end_of_game(guess, word, turn):
    if guess == word:
        return True
    if turn == GUESSES:
        return True
    return False


def display_letters_used(letters_used, guess):
    letters_used = list(guess + letters_used)
    letters_used = set(letters_used)
    return "".join(list(letters_used))


def populate_word_bank():
    # source of words:  https://github.com/dwyl/english-words/
    # written by Andy Miles
    with open('words_alpha.txt',
              'r') as w:
        words = w.readlines()

    five_chars = [word.strip() for word in words if len(word.strip()) == 5]

    return five_chars


def choose_wordbank_word(word_bank):
    return random.choice(word_bank)


def run_wordle():
    grid, color_grid = initialize_grid()
    word_bank = populate_word_bank()
    secret_word = choose_wordbank_word(word_bank)
    turn = 1
    letters_used = ""
    while True:
        display_grid(grid)
        print(" " * 9)
        display_grid(color_grid)
        guess = get_user_input()
        grid = populate_grid(guess, grid, turn)
        if check_end_of_game(guess, secret_word, turn):
            display_grid(grid)
            won = check_win_or_lose(guess, secret_word, turn)
            if won:
                print("You Win")
            else:
                print("You Lose")
            sys.exit()
        color_grid = change_cell_background_color(color_grid, grid, guess,
                                                  secret_word, turn)

        letters_used = display_letters_used(letters_used, guess)
        print(f"letters used: {letters_used}")
        turn += 1


if __name__ == "__main__":
    run_wordle()
