import random

def diceRoll():
    return random.randint(1, 6)

num = diceRoll()
print("A dice is rolled!")
lives = 5
points_awarded = 0
gameOver = False

while lives > 0 & gameOver == False:
    userGuess = int(input("Guess what number was rolled."))
    if userGuess == num:
        points_awarded += 10
        print("Congrats! The number was " + str(num) + "! Your point total is " + str(points_awarded) + ".")
        userWilling = input("Do you want to [C]ontinue?")
        if userWilling == "C" or userWilling == "c":
            print(" ")
            print("A new number was rolled.")
            print(" ")
            num = diceRoll()
        else:
            gameOver = True
    else:
        if lives != 1:
            lives -= 1
            print("Try again! You have " + str(lives) + " lives.")
            print(" ")
        else:
            print("You now have 0 lives. The correct number was " + str(num) + ". You get " + str(points_awarded) + " points.")
            lives = 0