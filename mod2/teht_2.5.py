#int заменить на float будет принимать дробное число

lu1 = float(input("Anna leiviskät"))
lu2 = float(input("Anna naulata"))
lu3 = float(input("Anna luodit"))

summa = (((lu1 * 20) + lu2) * 32 + lu3) * 13.3
kg, grams = divmod(summa, 1000)

print(f"Massa nykymittojen mukaan {kg:.0f} kilogrammaa {round(grams,2)} grammaa")