times = int(input("How many items would you like to add to the list"))
userList = []
for i in range (0, times):
    userInput = int(input("Add a number"))
    userList.append(userInput)
oneList = int(times/2)

A = []
B = []

if times%2==0:
    A = userList[:oneList]
    B = userList[oneList:]
else:
    A = userList[:oneList+1]
    B = userList[oneList:]

print("A is " + str(A))
print("B is " + str(B))