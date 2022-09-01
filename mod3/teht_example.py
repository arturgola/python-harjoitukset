# kahvi osto
# jos rahaa_taskussa>=5
# osta latte
# jos ei mutta rahaa_taskussa >=3
# osta normi kahvi
# muteen
# lähde pois

rahaa_taskussa = int(input("Paljonko sinulla on rahaa? "))
maistuuko_kahvi = input("Maistuuko kahvi? ")
latten_hinta = 5
kahvi_hinta = 3
teen_hinta = 2

if rahaa_taskussa >= latten_hinta and maistuuko_kahvi == "joo":
    print("Osta latte")
    print("juo latte")
    rahaa_taskussa = rahaa_taskussa - latten_hinta

elif rahaa_taskussa >= kahvi_hinta and maistuuko_kahvi == "joo":
    print("osta normikahvi")
    rahaa_taskussa = rahaa_taskussa - kahvi_hinta

elif rahaa_taskussa >= teen_hinta:
    print("ostan tee")
    rahaa_taskussa = rahaa_taskussa - teen_hinta

else:
    print("Lähden kotiin")

if rahaa_taskussa == 0:
    print("Rahat loppu")

else:
    print(f"Sinulla on vielä {rahaa_taskussa} euroa taskussa.")

