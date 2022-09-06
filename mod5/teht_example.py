nimet = ("Viivi", "Ahmed", "Pekka", "Olga", "Mary")

# tulostaa listan, jossa osa arvoista
print(nimet[0:4])
print(nimet[0:1])

#tulostaa yhden alkion arvon
print(nimet[0])
print(nimet[1])
print(nimet[2])

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# lista pituus eli koko
print(len(numbers))

# viimeisen alkion indeksi
print(numbers[len(numbers)-1])
print(numbers[-1])
# print(numbers[6]) [out of range error]

# listan kaikkien arvojen tulostus
for nimi in nimet:
    print(nimi)

userInput = input("Anna uusi nimi: ")
nimet.insert(1, userInput) # lisätään uusi arvo index-kohtaan 1
nimet.append(userInput)

# for nimi in nimet:

# saan iteraattoria i käyttäen
for i in range(len(nimet)):
    print(f"{i}. nimi: {nimet[i]}")

# tulostan kolmella jaolliset luvut välillä 0-1000
for i in range(0, 1001, 3):
    if i % 3 == 0:
        print(i)

letters = ["s", "a", "i", "p", "p", "u", "a", "k"]
letters2 = letters[0:len(letters)]
letters.reverse()
letters.extend(letters2)
print(letters)
word = ""
for letter in letters:
    word = word + letter
print(word)
