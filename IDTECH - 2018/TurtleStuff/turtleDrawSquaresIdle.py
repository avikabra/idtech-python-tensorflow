from turtle import *
from random import randint

designer = Turtle()
designer.penup()
designer.goto(-330, 330)

r, g, b = 0, 0, 0
colormode(255)

def chooseColor():

    global r, g, b
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    designer.pencolor(r, g, b)
    designer.fillcolor(r, g, b)
    print("The color is:", r, g, b)

def drawSquare(size):

    designer.begin_fill()
    designer.pendown()
    for i in range(4):
        designer.forward(size)
        designer.right(90)
    designer.penup()
    designer.end_fill()
    
def drawOneRow(number, size):

    for i in range(number):
        chooseColor()
        drawSquare(size)
        designer.forward(size)

def drawPattern(number, size):
    for j in range(number):
        drawOneRow(number, size)
        designer.backward(size*number)
        designer.right(90)
        designer.forward(size)
        designer.left(90)

userNumber = int(input("What would you like the size of the shapes to be?"))
userSize = int(input("How many squares per row would you like to draw?"))
drawPattern(userNumber, userSize)
