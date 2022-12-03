# Game settings file.
WALL = '+'
SPRITE = 'i'
SPRITE_T = 'I'

EMPTY = ' '
TARGET = 'o'
BOX_NS = '!'
BOX_S = '.'

RESTART = ' '
QUIT = 'q'

CONTROLS = "wasd q"

board = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, EMPTY, BOX_S, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
    [WALL, SPRITE, EMPTY, BOX_NS, EMPTY, TARGET, EMPTY, WALL],
    [WALL, EMPTY, EMPTY, EMPTY, BOX_NS, EMPTY, TARGET, WALL],
    [WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]
# main file
# from game_settings import *

for line in board:
    print(' '.join(line))
game_input = input()
while game_input in CONTROLS:
    if game_input == QUIT:
        print("Goodbye")
        break
    # if sokoban_input == 'w':
    # if sokoban_input == 's':
    if game_input == 'a':
        for line in board:
            for obj in range(len(line)):
                if line[obj] == SPRITE and line[obj - 1] == EMPTY:
                    line[obj] = EMPTY
                    line[obj - 1] = SPRITE
    if game_input == 'd':
        for line in board:
            for obj in range(len(line)):
                if line[obj] == SPRITE and line[obj + 1] == EMPTY:
                    line[obj] = EMPTY
                    line[obj + 1] = SPRITE

for line in board:
    print(' '.join(line))

# needs a main function
# needs the right logic in the right place in the loop
# draw_board()?
