import random

userStr = input("how many rolls?: ")
numOfRolls = int(userStr)

def rollDie():
    die = random.randint(1,6)
    print(die)

for roll in range(numOfRolls):
    rollDie()