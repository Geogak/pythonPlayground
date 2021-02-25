import random
from datetime import datetime
from csv import writer
def append_list_as_row(fileName, listOfElem):
    with open(fileName, 'a+', newline='') as writeObj:
        csvWriter = writer(writeObj)
        csvWriter.writerow(listOfElem)

print("hello world")
userName = input("what is your name? : ")
print("welcome ",userName)
num = random.randint(1,1000)
userGuess = 0
guessCount = 0 

while userGuess != num:
    guessCount += 1
    userGuess = int(input("guess a number between 1 and 1000 : "))
    if userGuess > num:
        print ("too high")
    if userGuess < num:
        print ("too low")

now = datetime.now()
ledgerEntry = [userName,guessCount,num,now]
append_list_as_row('scores.csv',ledgerEntry)
print("You guessed",num,"correctly in",guessCount,"tries!")