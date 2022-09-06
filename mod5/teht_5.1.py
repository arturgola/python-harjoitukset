import random

userInput = int(input("Give number of cubes: "))
sum = 0

for cube in range(userInput):
    sum += random.randint(1, 6)
print(f"summa of cubes is: {sum}")



