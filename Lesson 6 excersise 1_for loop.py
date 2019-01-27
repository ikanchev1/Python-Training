import random

compNum = random.randint(1,10)
success = 1
userGuess = int(input("Enter number between 1 and 10: "))

for i in range(1,5):
    if userGuess < compNum:
        print("My number is bigger!")
        userGuess = int(input("Enter number between 1 and 10: "))
    elif userGuess > compNum:
        print("My number is smaller!")
        userGuess = int(input("Enter number between 1 and 10: "))
    elif userGuess == compNum:
        print(f"Congratulations! You guessed my number is {compNum}")
        print(f"You guessed in {i} moves")
        success = 0
        break
    

if(success != 0):
    print(f"You lost! My number was {compNum}")
