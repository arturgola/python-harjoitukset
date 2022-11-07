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

    def drive(self, hours):
        self.odometer += hours * self.speed


class ElectricCar(Car):
    def __init__(self, register_number, max_speed, battery_capacity):
        super().__init__(register_number, max_speed)
        self.battery_capacity = battery_capacity

    def print_info(self):
        super().print_info()
        print(f"battery capacity: {self.battery_capacity} kWh.")


class GasolineCar(Car):
    def __init__(self, register_number, max_speed, tank_capacity):
        super().__init__(register_number, max_speed)
        self.tank_capacity = tank_capacity

    def print_info(self):
        super().print_info()
        print(f"tank capacity: {self.tank_capacity} l.")


tesla = ElectricCar(123, 220, 45);
tesla.accelerate(50)
tesla.drive(3)
gas = GasolineCar(223, 340, 10)
gas.accelerate(30)
gas.drive(3)
tesla.print_info()
gas.print_info()