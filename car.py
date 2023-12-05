
class Car:
    # Constructor
    def __init__(self, color, make):
        self._color = color
        self.make = make
        print("Hello")
        print(self)

    def get_color(self):
        # conditions fulfiled
        return self._color
    
    def set_color(self, color):
        self._color = color

    def run(self):
        print(f"{self.make} is running!!")



my_car = Car("black", "honda")

print(my_car.get_color)
my_car._color = "red"
print(my_car.make)

# my_car.run()

# your_car = Car("White", "Toyota")
# print(your_car.make)

# your_car.run()

class PetrolCar(Car):
    def __init__(self, color, make, capacity_of_tank):
        super().__init__(color,make)
        self.capacitity_of_tank = capacity_of_tank

    def make_turn(self):
        print("I am making a turn")



my_petrol_car = PetrolCar("silver", "BMW", 40)

print (my_petrol_car.make)

print (my_petrol_car.capacitity_of_tank)

my_petrol_car.run()


class ElectricCar(Car):
    #Overriding
    def run(self):
        print("I run silently")

my_electic_car = ElectricCar("Red", "Tesla")

my_electic_car.run()