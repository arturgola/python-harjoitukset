import random
diceNum = 0


def throwDice():
    return random.randint(1, 6)  # return как выполнит функцию, возвращает обратно ответ в начало


while diceNum != 6:
    diceNum = throwDice()
    print(f" rolled dice num is {diceNum}")
