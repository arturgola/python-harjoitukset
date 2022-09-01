hytti = input("Anna hyttiluokka LUX, A, B tai C muodossa:")

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")

if hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

if hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

if hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("virheellinen hyttiluokka, yrittää uudelleen")