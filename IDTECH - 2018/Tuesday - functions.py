#number swap
'''safety = 0

def swap(x, y):
    safety = x
    return y, safety

num1 = input("Enter one number")
num2 = input("Enter another number")

print("Number One is " + num1)
print("Number Two is " + num2)

num1, num2 = swap(num1, num2)

print("New number One is " + num1)
print("New number Two is " + num2)'''

#palindrome detector
palindrome = True
num=input("Enter a number")
temp = list(num)
reverse = []
length = len(temp)
for i in range(0, length):
    reverse.append(" ")
for i in range(0, length):
    reverse[i] = temp[length-1-i]

if reverse != temp:
    palindrome = False

print(palindrome)