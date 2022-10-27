class Koira:
    def __int__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koira_1 = Koira("Rekku", 2022)
koira_2 = Koira("Lao", 2015)

print (f"{koira_1.nimi:s} on syntynyt vuonna {koira_1.syntymävuosi:d}." )
print (f"{koira_2.nimi:s} on syntynyt vuonna {koira_2.syntymävuosi:d}." )