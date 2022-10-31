class Elevator:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor

    def floor_up(self):
        if (self.current_floor + 1 > self.max_floor):
            print(f"Elevator can't go pass max floor")
            return False

        self.current_floor += 1;
        print(f"Elevator now at floor:{self.current_floor}")
        return True

    def floor_down(self):
        if (self.current_floor - 1 < self.min_floor):
            print(f"Elevator can't go pass min floor")
            return False

        self.current_floor -= 1;
        print(f"Elevator now at floor:{self.current_floor}")
        return True

    def go_to_floor(self, floor):
        if (self.current_floor != floor):
            print(f"Elevator trying to go to floor {floor}")
        else:
            print(f"Elevator already at floor {floor}")

        while (self.current_floor != floor):
            if (floor > self.current_floor):
                if not self.floor_up():
                    return
            if (floor < self.current_floor):
                if not self.floor_down():
                    return


class Building:
    def __init__(self, min_floor, max_floor, elevators_amount):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = []
        self.elevators_amount = elevators_amount

        for i in range(0, elevators_amount - 1):
            self.elevators.append(Elevator(min_floor, max_floor))

        print(f"Building created with {elevators_amount} elevators, min floor is {min_floor}, max_floor is {max_floor}")

    def run_elevator(self, pos, floor):
        if (pos <= 0):
            print(f"Elevator {pos} doesn't exist")
            return

        print(f"Running {pos} elevator")
        self.elevators[pos - 1].go_to_floor(floor)


building = Building(0, 10, 10)
building.run_elevator(1, 5)
building.run_elevator(0, 5)