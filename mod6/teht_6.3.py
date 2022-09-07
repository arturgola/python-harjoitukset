userInput = int(input("Type amount in gallons: "))


def to_liters(gallons):
    return gallons * 3.7


while userInput > 0:
    print(f"{userInput} gallons will be {to_liters(userInput):.1f} in liters.")
    userInput = int(input("Type amount in gallons: "))
print("Wrong amount of gallons")

