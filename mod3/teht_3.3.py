
gender = input("Sukupuolise (nainen/mies)? ")
hg_value = int(input("Hemoglobiinisi (g/l)? "))

if gender == "nainen":
    #testataan arvojen järkevyys
    if (5 < hg_value > 300):
        print("virheellinen hemoglobiiniarvo!")
    #testataan naisen ohjearvot
    if hg_value < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif gender == "mies":
    #testataan arvojen järkevyys
    if (5 < hg_value > 300):
        print("virheellinen hemoglobiiniarvo!")
    #testataan miehen ohjearvot
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hg_value <= 195:
        print("Hemoglobiiniarvo normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")