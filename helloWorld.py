import random

print("hello world")
userInput = input("what is your name? : ")
print("welcome ",userInput)
num = random.randint(1,1000)
userGuess = 0
while userGuess != num:
    userGuess = int(input("guess a number between 1 and 1000 : "))
    if userGuess > num:
        print ("too high")
    if userGuess < num:
        print ("too low")
print(num)