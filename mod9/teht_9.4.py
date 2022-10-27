import random


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


def largest_millage(arr, n):
    max = arr[0].max_speed
    car = arr[0]

    for i in range(1, n):
        if arr[i].max_speed > max:
            max = arr[i].max_speed
            car = arr[i]
    return car


cars = []

for i in range(10):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

while True:
    for i in range(10):
        cars[i].accelerate(random.randint(-10, 15))
        cars[i].drive(1)

    leader = largest_millage(cars, len(cars))
    if leader.odometer >= 10000:
        print(f"{leader.register_number} won!")
        leader.print_info()
        break