'''num = 5
print(num != 5)
#>, <, >=, <=, !=, ==

if True:
    print("yay")
else:
    print("oh no")'''

'''for i in range(101):
    if (i%2 ==0):
        print(i)

userNum = int(input("Enter a number"))
if userNum%2==0:
    print("your number is even")
elif userNum%2==1:
    print("Your number is odd")
else:
    print("invalid number")'''

#

userNum = int(input("Enter a number"))

if userNum % 3 == 0:
    if userNum % 5 == 0:
        print("Your number is divisible by both 5 and 3")
    else:
        print("Your number is divisible by only 3")
else:
    if userNum % 5 == 0:
        print("Your number is divisible by only 5")
    else:
        print("Your number is not divisible by 3 or 5")