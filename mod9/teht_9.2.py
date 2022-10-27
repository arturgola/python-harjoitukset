class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton {self.register_number} "
              f"huippunopeus on {self.max_speed} km/h, "
              f"matkamittari: {self.odometer} km, "
              f"tämänhetkinen nopeus: {self.speed} km/h. ")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change >= self.max_speed:
            self.speed = self.max_speed

    def print_curSpeed(self):
        print(f"Car speed is {self.speed} km/h")

someCar = Car("ABC-1", 180)
someCar.accelerate(30)
someCar.accelerate(70)
someCar.accelerate(50)
someCar.print_curSpeed()
print("Pressing breaks")
someCar.accelerate(-200)
someCar.print_curSpeed()


