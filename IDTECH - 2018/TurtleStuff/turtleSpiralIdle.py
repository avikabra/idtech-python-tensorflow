from turtle import *
from random import randint


speed(0)
bgcolor('black')
pencolor('pink')

x = 0

while x < 400:

    fd(50 + x)
    rt(46)

    x += 1

exitonclick()
