import turtle
from turtle import *
from random import *

t = turtle.Turtle()

speed(0)  #fastest speed
t.pencolor('pink')
bgcolor('black')

y = 0
x = 0

t.penup()
t.left(180)
t.forward(100)
t.right(90)
t.pendown()

while y < 5:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    x = 0

    while x<30:

        #r = randint(0, 255)
        #g = randint(0, 255)
        #b = randint(0, 255)

        #colormode(255)
        #t.pencolor(r, g, b)
        
        for i in range(6):
            t.forward((y+1)*40)
            t.right(60)

        t.right(12.25)
        x += 1

    y += 1

exitonclick()
