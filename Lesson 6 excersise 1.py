import random

compNum = random.randint(1,10)

count = 1
maxTries = 5
success = 0

userGuess = int(input("Enter number between 1 and 10: "))

while userGuess != compNum:
    count += 1
    if count > maxTries:
        print(f"You lost! My number was {compNum}")
        success = 1
        break
    if userGuess < compNum:
        print("My number is bigger!")
    elif userGuess > compNum:
        print("My number is smaller!")
    userGuess = int(input("Enter number between 1 and 10: "))

if(success == 0):
    print(f"Congratulations! You guessed my number is {compNum}")
    print(f"You guessed in {count} moves")

