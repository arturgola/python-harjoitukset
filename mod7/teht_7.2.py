names = set()
name = input("type name: ")
while name != "":
    if name in names:
        print("Alredy given name")
    else:
        names.add(name)
        print(name)

    name = input("Type new name: ")

for i in names:
    print(i)

