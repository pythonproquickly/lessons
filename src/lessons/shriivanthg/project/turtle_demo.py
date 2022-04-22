import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title("Wordle")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0, 0)
screen.bgcolor('black')
turtle.color('white')

gs = 0
state = []
for i in range(6):
    state.append([-1] * 5)


def draw_square(coord, s, fc='black'):
    turtle.up()
    x = coord[0]
    y = coord[1]
    turtle.goto(x - s / 2, y - s / 2)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(fc)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(s)
        turtle.left(90)
    turtle.end_fill()


def get_coord(i, j):
    return -200 + 100 * j, 300 - 100 * i


def draw_board():
    turtle.pencolor('dark gray')
    for i in range(6):
        for j in range(5):
            draw_square(get_coord(i, j), 80)


def display_word(w):
    turtle.up()
    turtle.color('white')
    for i in range(5):
        x, y = get_coord(gs, i)
        turtle.goto(x, y - 23)
        turtle.write(w[i].upper(), align='center', font=('Arial', 40, 'bold'))


def update_cell(i, j):
    global word, state
    x, y = get_coord(i, j)
    turtle.pencolor('dark gray')
    if state[i][j] == 0:
        fc = 'dark gray'
    elif state[i][j] == 1:
        fc = 'goldenrod'
    else:
        fc = 'green'
    draw_square(get_coord(i, j), 80, fc)
    turtle.up()
    turtle.color('white')
    turtle.goto(x, y - 23)
    turtle.write(word[j].upper(), align='center', font=('Arial', 40, 'bold'))
    screen.update()


word = 'abcde'
draw_board()
display_word(word)
screen.update()
screen.listen()
screen.mainloop()
