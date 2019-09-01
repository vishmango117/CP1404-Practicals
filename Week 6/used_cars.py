"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car

def randomshit():
    """Demo test code to show how to use car class."""
    my_car = Car("Default",180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

def the_good_stuff():
    car_limo = Car("Limo", 100)
    print(car_limo)
    car_limo.add_fuel(20)
    print(car_limo)
    car_limo.drive(115)
    print(car_limo)


def main():
    randomshit()
    the_good_stuff()

if __name__ == "__main__":
    main()