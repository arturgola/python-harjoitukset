number = int(input("Type a number: "))
flag = False

if number > 1:
    for i in range(2, number): # цикл от 2 чтобы попробовать поделить это число
        if (number % i) == 0:
            flag = True
            break

if flag:
    print(number, "ei ole alkuluku")
else:
    print(number, "on alkuluku")