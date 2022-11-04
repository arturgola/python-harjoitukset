class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.odometer = 0

    def accelerate(self):
        self.speed += 1

    def print_info(self):
        print(f"{self.name}: speed: {self.speed}, odometer: {self.odometer}")

class Bike(Vehicle):
    def __init__(self, name, gears):
        super().__init__(name)
        self.number_of_gear = gears
    def print_info(self):
        super().print_info()
        print(f"Number of gears: {self.number_of_gear}")

class Car(Vehicle):
    def __init__(self, name, gas_level):
        super().__init__(name)
        self.gas_level = gas_level
    def accelerate(self):
        super().accelerate()
        self.speed += 5
        self.gas_level -= 1
    def print_info(self):
        super().print_info()
        print(f"Gas level: {self.gas_level}")

v1 = Car("Rally car", 30)
v1.accelerate()
v1.print_info()
v2 = Bike("Jopo", 1)
v2.accelerate()
v2.print_info()
