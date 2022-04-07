import turtle
import random

s = turtle.Screen()
s.setup(1200, 800)
s.colormode(255)
draw = turtle.Turtle()
draw.speed(0)
s.bgcolor("grey")
draw.pencolor("black")
draw.pensize(5)


def drawAmongUs():
    # draw command go here...
    draw.forward(50)
    draw.left(90)  # turn left 90 degrees
    draw.forward(70)
    draw.left(90)
    draw.forward(50)
    draw.left(90)
    draw.forward(70)


def drawGlass():
    # draw glass commands go here
    pass


y = int(s.numinput("Among Us!", "Please input how many Among Us characters you want: "))

for x in range(y):
    drawAmongUs()


turtle.done()
