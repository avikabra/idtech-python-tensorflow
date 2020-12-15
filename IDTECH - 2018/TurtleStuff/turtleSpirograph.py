from turtle import *
import time
from random import randint

designer = Turtle()

designer.speed(5)
designer.pencolor('pink')

colors = ['red', 'blue', 'green', 'orange', 'cyan', 'purple', 'pink', 'white', 'black', 'yellow']

x = 0

while x < 200:

    colorPicker = randint(0, 9)
    designer.fillcolor(colors[colorPicker])

    designer.begin_fill()

    for i in range(3):
        designer.forward(50 + (5 * x))
        designer.right(120)

    designer.end_fill()

    designer.right(19)

time.sleep(5)