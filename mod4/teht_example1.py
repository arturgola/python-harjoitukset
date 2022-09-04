import random

numberOfRounds = 2
# numberOfRounds = int(input("Monta numeroa luupataan?: "))

i = 0

while i < numberOfRounds: # ehdosta tulee aina arvo True tai False
    i += 1
    # i+=2 # i=i+2
    # tulostetaan parittomat luvut
    print(f"i = {i - 1} + 1 -> {i}")
    if i % 2 == 1:
        print(f"{i} on pariton")
print(f"i:n arvo silmukan jälkeen {i}")

# "Tekstikäyttöliittymällisen ohjelman valikko"

command = ""

while True:
    coomand = input("Komento")
    command = command.lower()
    if command == "tulosta":
        print("printtaillaan jotain")
    elif command == "piirrä" or coomand == "Pirrä":
        i = 0
        while i < 3:
            i += 1
            print("######")
    elif command == "lopeta":
        print("lopetetaan ohjelma. Heippa!")
    elif command == "pelaa noppa"
        noppa1 = noppa2 = heitot = 0
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        heitot = heitot + 1
    toistot = toistot

    else:
        print(f"Virheellinen komenti, yritä uudelleen.")
print("")