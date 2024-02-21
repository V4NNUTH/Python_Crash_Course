class Car:
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
            
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milleage):
        if milleage >= self.odometer_reading:
            self.odometer_reading = milleage
        else:
            print("You can't roll back  an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

new_car = Car('tesla','a5',2022)
print(new_car.get_descriptive_name())

new_car.update_odometer(35)

##new_car.odometer_reading = 23
new_car.read_odometer()

new_car.increment_odometer(14)
new_car.read_odometer()
