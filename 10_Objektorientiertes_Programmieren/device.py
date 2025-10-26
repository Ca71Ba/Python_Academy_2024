class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def main_functionality(self):
        print("This device performs its main functionality.")

class Vacuum_Cleaner(Device):
    def __init__(self, brand, power):
        super().__init__(brand)
        self.power = power

    def clean(self):
        print(f"The {self.brand} vacuum cleaner is cleaning the floor with {self.power} watts of power.")

    def main_functionality(self):
        print("This vacuum cleaner is designed for cleaning.")

class Water_Boiler(Device):
    def __init__(self, brand, power, fluid_type="Water"):
        super().__init__(brand)
        self.power = power
        self.fluid_type = fluid_type

    def boil(self):
        print(f"The {self.brand} water boiler is heating up {self.fluid_type} with {self.power} watts of power.")

    def main_functionality(self):
        print(f"This water boiler is boiling {self.fluid_type}.")