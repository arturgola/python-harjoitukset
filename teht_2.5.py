lu1 = int(input("Anna leiviskät"))
lu2 = int(input("Anna naulata"))
lu3 = int(input("Anna luodit"))

summa = (((lu1 * 20) + lu2) * 32 + lu3) * 13.3
kg, grams = divmod(summa, 1000)

print(f"Massa nykymittojen mukaan {kg} kilogrammaa {round(grams,2)} grammaa")

