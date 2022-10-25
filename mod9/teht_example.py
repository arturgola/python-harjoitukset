'''
class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koira = Koira("Rekku", 2022)

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." )
'''

class Car:
    def __int__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton {self.register_number} "
              f"huippunopeus on {self.max_speed} km/h, "
              f"matkamittari: {self.odometer} km, "
              f"tämänhetkinen nopeus: {self.speed} km/h. ")

    def accelerate(self):
        self.speed = self.speed + 3


someCar = Car("ABC-1", 120)
otherCar = Car("ABC-2", 150)
otherCar.accelerate()
otherCar.accelerate()
someCar.print_info()
otherCar.print_info()


