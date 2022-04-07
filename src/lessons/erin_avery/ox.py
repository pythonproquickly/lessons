# XXX and OOO

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

# example only - comment this out
# X in middle top row

# O in last column of bottom row
board[2][0] = 'O'
board[1][1] = 'O'
board[0][2] = 'O'
# end of comment out
print(board)
# check if a row wins

player = "O"

# check if row wins
for row in range(len(board)):
    win = True
    for col in range(len(board)):
        if board[row][col] != player:
            win = False
            break
    if win:
        break

# check if a column wins
if not win:
    for row in range(len(board)):
        win = True
        for col in range(len(board)):
            if board[col][row] != player:
                win = False
                break
        if win:
            break

# check if a diagonal wins
if not win:
    win = True
    for row in range(len(board)):
        if board[row][row] != player:
            win = False
            break
    if not win:
        win = True
        for row in range(len(board)):
            if board[row][len(board) - 1 - row] != player:
                win = False
                break
        if not win:
            win = True
            for row in board:
                for item in row:
                    if item == ' ':
                        win = False
                        break
print(win)
