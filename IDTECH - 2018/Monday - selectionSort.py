userList = []

times = int(input("How many items would you like to add to the list"))
for i in range (0, times):
    userInput = int(input("Add a number"))
    userList.append(userInput)

#sorting
newList = []
minimum = -999

for i in range(0, times):
    for i in range(1, len(userList)):
        if userList[i-1]>minimum:
            minimum = i-1
    newList[minimum, userList[minimum]]
    userList.pop(minimum)

print("New List: " + str(newList))