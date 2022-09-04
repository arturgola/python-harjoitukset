userId = "python"
password = "rules"
attempts = 1

while attempts <= 5:
    guess = input("Anna käyttäjätunnus ")
    if guess != userId:
        print("Väärä käyttäjätunnus")
        attempts += 1
        continue
    guess = input("Anna salasana ")
    if guess != password:
        print("Väärä salasana")
        attempts += 1
        continue
    print("Tervetuloa")
    break

if attempts > 5:
    print("Pääsy evätty")
