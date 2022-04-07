import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Os and Xs")
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor('light blue')
screen.tracer(0, 0)
turtle.hideturtle()


def draw(board):
    turtle.pencolor('black')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3, -1)
    turtle.setheading(0)
    turtle.down()
    turtle.forward(6)
    turtle.up()
    turtle.goto(-3, 1)
    turtle.setheading(0)
    turtle.down()
    turtle.forward(6)
    turtle.up()
    turtle.goto(-1, -3)
    turtle.setheading(90)
    turtle.down()
    turtle.forward(6)
    turtle.up()
    turtle.goto(1, -3)
    turtle.setheading(90)
    turtle.down()
    turtle.forward(6)
    board_size = len(board)
    for pos1 in range(board_size):
        for pos2 in range(board_size):
            draw_piece(pos1, pos2, board[pos1][pos2])
    screen.update()


def draw_piece(pos1, pos2, piece):
    if piece == 0:
        return
    x = 2 * (pos2 - 1)
    y = -2 * (pos1 - 1)
    if piece == 1:
        turtle.color('blue')
        turtle.up()
        turtle.goto(x - 0.75, y - 0.75)
        turtle.down()
        turtle.goto(x + 0.75, y + 0.75)
        turtle.up()
        turtle.goto(x - 0.75, y + 0.75)
        turtle.down()
        turtle.goto(x + 0.75, y - 0.75)
    else:
        turtle.up()
        turtle.goto(x, y - 0.75)
        turtle.setheading(0)
        turtle.color('red')
        turtle.down()
        turtle.circle(0.75)


def check_game(board):
    if board[0][0] > 0 and \
            board[0][0] == board[0][1] and \
            board[0][1] == board[0][2]:
        return board[0][0]

    if board[1][0] > 0 and \
            board[1][0] == board[1][1] and \
            board[1][1] == board[1][2]:
        return board[1][0]

    if board[2][0] > 0 and \
            board[2][0] == board[2][1] and \
            board[2][1] == board[2][2]:
        return board[2][0]

    if board[0][0] > 0 and \
            board[0][0] == board[1][0] and \
            board[1][0] == board[2][0]:
        return board[0][0]

    if board[0][1] > 0 and \
            board[0][1] == board[1][1] and \
            board[1][1] == board[2][1]:
        return board[0][1]

    if board[0][2] > 0 and \
            board[0][2] == board[1][2] and \
            board[1][2] == board[2][2]:
        return board[0][2]

    if board[0][0] > 0 and \
            board[0][0] == board[1][1] and \
            board[1][1] == board[2][2]:
        return board[0][0]

    if board[2][0] > 0 and \
            board[2][0] == board[1][1] and \
            board[1][1] == board[0][2]:
        return board[2][0]


def game_status(board):
    board_size = len(board)
    not_empty = 0
    for pos1 in range(board_size):
        for pos2 in range(board_size):
            if board[pos1][pos2] > 0:
                not_empty = not_empty + 1
    if not_empty == 9:
        return 3
    else:
        return 0


def find_result(result):
    if result == 1:
        return "X won!, game over"
    elif result == 2:
        return "O won!, game over"
    elif result == 3:
        return "No one won, Game over"
    else:
        return ""


def play_game(x, y):
    global turn
    pos1 = 3 - int(y + 5) // 2
    pos2 = int(x + 5) // 2 - 1
    if turn == 'X':
        board[pos1][pos2] = 1
        turn = 'O'
    else:
        board[pos1][pos2] = 2
        turn = 'X'
    draw(board)
    result = check_game(board)
    if result is None:
        result = game_status(board)
    over_message = find_result(result)
    if over_message != "":
        screen.textinput("The end", over_message)


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
draw(board)
turn = 'X'
screen.onclick(play_game)
turtle.mainloop()
