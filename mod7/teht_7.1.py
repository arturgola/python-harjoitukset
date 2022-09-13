inp = int(input("input value"))

seasons = {1: "winter", 2: "winter", 3: "autumn", 4: "autumn", 5: "autumn",
           6: "summer", 7: "summer", 8: "summer", 9: "spring", 10: "spring",
           11: "spring", 12: "winter"}

if inp in seasons:
    print(seasons[inp])
else:
    print(f"{inp} is bad value")