userList = []

times = int(input("How many items would you like to add to the list"))
for i in range (0, times):
    userInput = int(input("Add a number"))
    userList.append(userInput)

safety = 0

def swap(y, x):
    safety = y
    y = x
    x = safety


print("Old List: " + str(userList))

#sorting
for i in range(1, times):
    for i in range (0, times-1):
        if userList[i] > userList[i+1]:
            userList[i], userList[i + 1] =  userList[i+1], userList[i]

print("New List: " + str(userList))