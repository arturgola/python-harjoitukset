# Yksi leiviskä on 20 фунт.
# Yksi фунт on 32 лот.
# Yksi лот on 13,3 grammaa.

lu1 = int(input("Anna leivisköintä"))
lu2 = int(input("Anna nauloita"))
lu3 = int(input("Anna luoteita"))

summa = (((lu1 * 20) + lu2) * 32 + lu3) * 13.3
kg, grams = divmod(summa, 1000)

print(f"Massa nykymittojen mukaan {kg} kilogrammaa {round(grams,2)} grammaa")

