import random
from datetime import datetime
from csv import writer

def append_list_as_row(fileName, listOfElem):
    with open(fileName, 'a+', newline='') as writeObj:
        csvWriter = writer(writeObj)
        csvWriter.writerow(listOfElem)

print("Guess The Number Game!")
userName = input("what is your name? : ")
print("welcome ",userName)
minNum = 1
maxNum = input("Choose a max number : ")
num = random.randint(minNum,int(maxNum))
userGuess = 0
guessCount = 0 
promptString = "guess a number between " + str(minNum) + " and " + str(maxNum) + ": "

while userGuess != num:
    guessCount += 1
    userGuess = int(input(promptString))
    if userGuess > num:
        print ("too high")
    if userGuess < num:
        print ("too low")

now = datetime.now()
ledgerEntry = [userName,guessCount,num,now]
append_list_as_row('scores.csv',ledgerEntry)
print("You guessed",num,"correctly in",guessCount,"tries!")