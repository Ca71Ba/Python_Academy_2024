# Object Oriented Programming (OOP) in Python

from device import Device, Vacuum_Cleaner, Water_Boiler

my_device = Device("TechBrand")
my_device.main_functionality()

my_cleaner = Vacuum_Cleaner("CleanMaster", 1000)
my_cleaner.clean()  
my_cleaner.main_functionality()

my_boiler = Water_Boiler("BoilMaster", 1500, "Oil")
# my_boiler = Water_Boiler("BoilMaster", 1500)
my_boiler.boil()
my_boiler.main_functionality()


