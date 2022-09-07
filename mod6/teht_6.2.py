import random
diceNum = 0
diceEdges = int(input("Type edges amount: "))

def throwDice(maxEdges):
    return random.randint(1, maxEdges)

while diceNum != diceEdges:
    diceNum = throwDice(diceEdges)
    print(f" rolled dice num is {diceNum}")