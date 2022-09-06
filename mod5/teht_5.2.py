userInput = int(input("Enter number: "))
numbers = [userInput]


for number in numbers:
    userInput = input("Enter number: ")
    if userInput == "":
        break
    numbers.append(int(userInput))

numbers.sort(reverse=True)

print(numbers[:5])
