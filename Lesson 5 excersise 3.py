import random

compNum = random.randint(1,10)

count = 1

userGuess = int(input("Enter number between 1 and 10: "))

while userGuess != compNum:
    count += 1
    if userGuess < compNum:
        print("My number is bigger!")
    elif userGuess > compNum:
        print("My number is smaller!")
    userGuess = int(input("Enter number between 1 and 10: "))

print(f"Congratulations! You guessed my number is {compNum}")
print(f"You guessed in {count} moves")
