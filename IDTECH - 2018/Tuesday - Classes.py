#Area of a rectangle

'''class rectanglearea:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        return self.area

user1 = int(input("What would the length be?"))
user2 = int(input("And the width?"))
a = rectanglearea(user1, user2)

print(a.area())'''

#employee

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class employee(person):

    def __init__(self, name, age, employeeID, salary):
        super().__init__(name, age)
        self.ID = employeeID
        self.salary = salary

    def getID(self):
        return self.ID

    def getSalary(self):
        return self.salary

    def giveRaise(self, money):
        self.salary += money

userInput1 = input("What's your name")

avi = employee(userInput1, 13, 1, 5000)

print(avi.getName())
print(avi.getID())
print(avi.getSalary())
avi.giveRaise(30)
print(avi.getSalary())