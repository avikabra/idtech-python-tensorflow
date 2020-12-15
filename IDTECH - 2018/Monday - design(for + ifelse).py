num = int(input("enter the number of rows"))
numIncrease = 1
counter = num
num2 = num

#decreasing order
while num != 0:
    for i in range (1, num+1):
        print("*", end= " ")
    num -= 1
    print(" ")

print(" ")
print(" ")

#increasing order
while numIncrease<counter+1:
    for i in range (1, num2):
        print(" ", end= " ")
    for i in range (numIncrease, 0, -1):
        print("*", end= " ")
    numIncrease += 1
    num2 -= 1
    print(" ")