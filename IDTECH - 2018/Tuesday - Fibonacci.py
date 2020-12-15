num1 = 1
num2 = 1
sum = num1 + num2
userWilling = "C"

print(num1)

while sum != 0:
    print(num2)
    num1 = num2
    num2 = sum
    sum = num1 + num2
    userWilling = input("Do you want to continue?")
    if userWilling == "Yes" or userWilling == "yes":
        print(" ")
    else:
        print("OK")
        sum = 0