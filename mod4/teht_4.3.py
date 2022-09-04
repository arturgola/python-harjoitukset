# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

userinput = input("Sano luku: ")
maxValue = minValue = int(userinput)

while userinput != "":
    userinput = input("Sano luku: ")
    if userinput == "":
        break
    userinput = int(userinput)
    if int(userinput) < minValue:
        minValue = userinput
    if userinput > maxValue:
        maxValue = userinput
print(f"Pienin arvo: {minValue}, suurin arvo: {maxValue}")
