import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='admin',
         password= 'admin1?',
         autocommit=True
         )

maakoodi = input("Kirjoita maakoodi")
sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = '" + maakoodi + "' GROUP BY TYPE"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")