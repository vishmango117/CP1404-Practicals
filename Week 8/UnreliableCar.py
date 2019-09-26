import random
from Car import Car

class UnreliableCar(Car):
    
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation of a Unreliable Car object."""
        return "{}, fuel={}, odometer={} reliability= {}%".format(self.name, self.fuel,
                                                 self.odometer, self.reliability)


    def drive(self, distance):
        distance_travelled = 0
        if(self.reliability < random.randint(0,100)):
           distance_travelled = super().drive(distance)
        return distance_travelled

        
        
           

