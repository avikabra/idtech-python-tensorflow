import turtle
import time

t = turtle.Turtle()
x = 0

t.speed(0)
turtle.bgcolor('black')
t.pencolor('pink')

while x < 400:
    t.forward(50 + x)
    t.right(91)
    x += 1
time.sleep(5)