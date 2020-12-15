list_of_numbers = [2, 1, 3, 4, 5]
list_of_strings = ["hola", "hi", "namaste"]

list_of_strings.sort()
list_of_numbers.sort()

print(list_of_strings)
print(list_of_numbers)

#tuples can't be changed, don't even try

modify = (1, 2, 4)
print(modify)

userList = []

times = int(input("How many items would you like to add to the list"))
for i in range (0, times):
    userInput = int(input("Add a number"))
    userList.append(userInput)