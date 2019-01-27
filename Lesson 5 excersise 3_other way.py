import random

compNum = random.randint(1,10)
count = 0

def guess():
    global count
    count += 1
    try:
       userGuess = int(input("Enter number between 1 and 10: "))
    except ValueError:
       print("This is not valid integer number")
       guess()

    if userGuess < compNum:
        print("My number is bigger!")
        guess()
    elif userGuess > compNum:
        print("My number is smaller!")
        guess()
    elif userGuess == compNum:
        print(f"Congratulations! You guessed my number is {compNum}")
    return count

guess()
print(f"You guessed in {count} moves")
