import random

numberToGuess = random.randint(1, 10)
print("I guessed a number in range between 1 to 10, try to guessed it!")

while True:
    guessedNumber = int(input("Type number: "))
    if guessedNumber > numberToGuess:
        print("U guess is too big")
        continue
    if guessedNumber < numberToGuess:
        print("U guess is too low")
        continue
    if guessedNumber == numberToGuess:
        print("U guess is correct")
        break
