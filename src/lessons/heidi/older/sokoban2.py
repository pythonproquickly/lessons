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

# ---------

starting_board = copy.deepcopy(board)
for line in board:
    print(' '.join(line))
print()

while True:
    game_input = input()
    if game_input == QUIT:
        print("Goodbye")
        break
    elif game_input == RESTART:
        board = copy.deepcopy(starting_board)
        print("restarting...")
        for line in board:
            print(' '.join(line))

        print()
        continue
    elif game_input == 'w':
        condition = True
        for line in range(len(board)):
            for obj in range(len(board[line])):
                if condition == True and board[line][obj] == SPRITE and \
                        board[line - 1][obj] == EMPTY:
                    board[line][obj] = EMPTY
                    board[line - 1][obj] = SPRITE
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line - 1][obj] == BOX_NS and board[line - 2][
                    obj] == EMPTY:
                    board[line][obj] = EMPTY
                    board[line - 1][obj] = SPRITE
                    board[line - 2][obj] = BOX_NS
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line - 1][obj] == BOX_NS and board[line - 2][
                    obj] == TARGET:
                    board[line][obj] = EMPTY
                    board[line - 1][obj] = SPRITE
                    board[line - 2][obj] = BOX_S
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line - 1][obj] == BOX_S and board[line - 2][
                    obj] == EMPTY:
                    board[line][obj] = EMPTY
                    board[line - 1][obj] = SPRITE_T
                    board[line - 2][obj] = BOX_NS
                    condition = False
    elif game_input == 's':
        condition = True
        for line in range(len(board)):
            for obj in range(len(board[line])):
                if condition == True and board[line][obj] == SPRITE and \
                        board[line + 1][obj] == EMPTY:
                    board[line][obj] = EMPTY
                    board[line + 1][obj] = SPRITE
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line + 1][obj] == BOX_NS and board[line + 2][
                    obj] == EMPTY:
                    board[line][obj] = EMPTY
                    board[line + 1][obj] = SPRITE
                    board[line + 2][obj] = BOX_NS
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line + 1][obj] == BOX_NS and board[line + 2][
                    obj] == TARGET:
                    board[line][obj] = EMPTY
                    board[line + 1][obj] = SPRITE
                    board[line + 2][obj] = BOX_S
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line + 1][obj] == BOX_S and board[line + 2][
                    obj] == EMPTY:
                    board[line][obj] = EMPTY
                    board[line + 1][obj] = SPRITE_T
                    board[line + 2][obj] = BOX_NS
                    condition = False
                elif condition == True and board[line][obj] == SPRITE and \
                        board[line + 1][obj] == TARGET:
                    board[line][obj] = EMPTY
                    board[line + 1][obj] = SPRITE_T
                    condition = False
    elif game_input == 'd':
        condition = True
        for line in board:
            for obj in range(len(line)):
                if condition == True and line[obj] == SPRITE and \
                        line[obj + 1] == EMPTY:
                    line[obj] = EMPTY
                    line[obj + 1] = SPRITE
                    condition = False
                elif condition == True and line[obj] == SPRITE and line[
                    obj + 1] == BOX_NS and line[obj + 2] == EMPTY:
                    line[obj] = EMPTY
                    line[obj + 1] = SPRITE
                    line[obj + 2] = BOX_NS
                    condition = False
                elif condition == True and line[obj] == SPRITE and line[
                    obj + 1] == BOX_NS and line[obj + 2] == TARGET:
                    line[obj] = EMPTY
                    line[obj + 1] = SPRITE
                    line[obj + 2] = BOX_S
                    condition = False
                elif condition == True and line[obj] == SPRITE and line[
                    obj + 1] == BOX_S and line[obj + 2] == EMPTY:
                    line[obj] = EMPTY
                    line[obj + 1] = SPRITE_T
                    line[obj + 2] = BOX_NS
                    condition = False
                elif condition == True and line[obj] == SPRITE_T and line[
                    obj + 1] == EMPTY:
                    line[obj] = TARGET
                    line[obj + 1] = SPRITE
                    condition = False
                elif condition == True and line[obj] == SPRITE_T and line[
                    obj + 1] == BOX_NS and line[obj + 2] == EMPTY:
                    line[obj] = TARGET
                    line[obj + 1] = SPRITE
                    line[obj + 2] = BOX_NS
                    condition = False
    elif game_input == 'a':
        condition = True
        for line in board:
            for obj in range(len(line)):
                if condition == True and line[obj] == SPRITE and \
                        line[obj - 1] == EMPTY:
                    line[obj] = EMPTY
                    line[obj - 1] = SPRITE
                    condition = False
                elif condition == True and line[obj] == SPRITE and line[
                    obj - 1] == BOX_NS and line[obj - 2] == EMPTY:
                    line[obj] = EMPTY
                    line[obj - 1] = SPRITE
                    line[obj - 2] = BOX_NS
                    condition = False
                elif condition == True and line[obj] == SPRITE and line[
                    obj - 1] == BOX_NS and line[obj - 2] == TARGET:
                    line[obj] = EMPTY
                    line[obj - 1] = SPRITE
                    line[obj - 2] = BOX_S
                    condition = False
                elif condition == True and line[obj] == SPRITE and line[
                    obj - 1] == BOX_S and line[obj - 2] == EMPTY:
                    line[obj] = EMPTY
                    line[obj - 1] = SPRITE_T
                    line[obj - 2] = BOX_NS
                    condition = False
                elif condition == True and line[obj] == SPRITE_T and line[
                    obj - 1] == EMPTY:
                    line[obj] = TARGET
                    line[obj - 1] = SPRITE
                    condition = False
    count_box = 0
    for line in board:
        for obj in line:
            if obj == BOX_S:
                count_box += 1
    if game_input in CONTROLS and count_box != 3:
        for line in board:
            print(' '.join(line))
        print()
    elif count_box == 3:
        for line in board:
            print(' '.join(line))
        print("You Win!")
        break
    else:
        print("enter a valid move:")
