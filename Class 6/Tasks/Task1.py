# 1.
# Create a class called "Car" with attributes like "make," "model," and "year."
# Create an instance of the Car class and print its attributes.
# Add a method to the Car class that calculates the car's age based on the current year.
# Create a subclass of Car called "ElectricCar" with an additional attribute for battery capacity.
# Override the Car class's method in the ElectricCar subclass to also calculate the remaining battery life.
from datetime import datetime


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_age(self):
        current_year = datetime.now().year
        return current_year - int(self.year)


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def car_age(self):
        current_year = datetime.now().year
        battery_life = self.battery_capacity / 2
        return current_year - int(self.year), battery_life


volkswagen = Car('Volkswagen', 'Golf', '2017')
e_volkswagen = ElectricCar("Volkswagen", "e-Golf", '2023', 999)

print(volkswagen.make)
print(volkswagen.model)
print(volkswagen.year)
print(volkswagen.car_age())
print(e_volkswagen.car_age())
