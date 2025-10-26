class Vehicle:
    def __init__(self, max_speed, door_count):
        self.max_speed = max_speed
        self.door_count = door_count

    def drive(self):
        print(f"The vehicle is driving at a max speed of {self.max_speed} km/h.")


class Plane(Vehicle):
    def __init__(self, max_speed, door_count, wing_span):
        super().__init__(max_speed, door_count)
        self.wing_span = wing_span
        
    def start_landing(self):
        print("The plane is starting its landing sequence.")

    def drive(self):
        print(f"The plane is flying at max speed of {self.max_speed} km/h.")
