class Elevator:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        print(f"Elevator created, min floor is {self.min_floor}, max floor is {self.max_floor}")

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
        print(f"Elevator trying to go to floor {floor}")

        while (self.current_floor != floor):
            if (floor > self.current_floor):
                if not self.floor_up():
                    return
            if (floor < self.current_floor):
                if not self.floor_down():
                    return