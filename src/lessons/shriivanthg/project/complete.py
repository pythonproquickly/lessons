import random
import turtle
from tkinter import *
from tkinter import messagebox

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title("Wordle Solver - PythonTurtle.Academy")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0, 0)
screen.bgcolor('black')
turtle.color('white')

gs = 0
state = []
for i in range(6):
    state.append([-1] * 5)


def getwords(words, cs, count=False):
    res = []
    cnt = 0
    for w in words:
        t = list(w)
        flag = True
        cnt = dict()
        # first loop checks only positions are set
        for l, p in cs:
            if p < 0: continue
            if cs[(l, p)] > 0:
                if t[p] == l:
                    t[p] = '*'
                    if l in cnt:
                        cnt[l] += 1
                    else:
                        cnt[l] = 1
                else:
                    flag = False
                    break
            else:
                if t[p] == l:
                    flag = False
                    break
        if (not flag): continue
        # second loop checks only positions are not set
        for l, p in cs:
            if p != -1: continue
            v = 0 if l not in cnt else cnt[l]
            for _ in range(cs[(l, p)] - v):
                try:
                    p = t.index(l)
                    t[p] = '*'
                except ValueError:
                    flag = False
                    break
            if (not flag): break
        if (not flag): continue
        # third loops checks non-existent letter
        for l, p in cs:
            if p != -2: continue
            if l in t:
                flag = False
                break

        if flag:
            if count:
                cnt += 1
            else:
                res.append(w)
    if count:
        return cnt
    else:
        return res


def guess_random(words):
    return random.choice(words)


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
    global w, state
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
    turtle.write(w[j].upper(), align='center', font=('Arial', 40, 'bold'))
    screen.update()


def play(x, y):
    flag = False
    for i in range(6):
        if flag: break
        for j in range(5):
            cx, cy = get_coord(i, j)
            if (cx - x) ** 2 + (cy - y) ** 2 < 1600:
                flag = True
                ci = i
                cj = j
                break
    if not flag: return
    if ci != gs: return
    state[ci][cj] = (state[ci][cj] + 1) % 3
    update_cell(ci, cj)


def submit():
    global state
    global gs
    global w, words

    for i in range(5):
        if state[gs][i] == -1: return

    cs = dict()
    for i in range(5):
        if state[gs][i] == 0:  # letter doesn't exist
            cs[(w[i], -2)] = 1
        else:
            if (w[i], -1) not in cs:
                cs[(w[i], -1)] = 1
            else:
                cs[(w[i], -1)] += 1
            if state[gs][i] == 1:
                cs[(w[i], i)] = 0
            else:
                cs[(w[i], i)] = 1
    words = getwords(words, cs)
    print(len(words))
    w = guess_random(words)
    gs += 1
    display_word(w)
    if len(words) == 1:
        messagebox.showinfo("Done", "Congratulations!")
        turtle.bye()

    screen.update()


orig_words = []
f = open('wordle_words.txt', 'r')
for w in f:
    orig_words.append(w.strip())

cs = dict()
words = getwords(orig_words, cs)
w = guess_random(words)
w = 'tesla'
draw_board()
display_word(w)
screen.update()
screen.onclick(play)
screen.onkey(submit, 'Return')
screen.listen()
screen.mainloop()
