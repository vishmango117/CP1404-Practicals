"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""
    tank_cap = 0
    def __init__(self, name="Default", fuel=100):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.tank_cap = fuel
        self.fuel = fuel
        self.odometer = 0
        self.name = name
    
    def __str__(self):
        return "{}, {}, {}".format(self.name, self.fuel, self.odometer)
    
    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        if(amount+self.fuel <= self.tank_cap):
            self.fuel += amount
            print("Added {} units of fuel".format(amount))
        elif(amount+self.fuel > self.tank_cap):
            self.fuel = self.tank_cap
            print("Added {} units of fuel".format(self.tank_cap))


    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance