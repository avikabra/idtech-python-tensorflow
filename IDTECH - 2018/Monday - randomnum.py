import random

print("Rolling the dice!")

def random_num(max):
    return random.randint(1, max)

condition = False

while not condition:
    userNum = random_nunm(5);
