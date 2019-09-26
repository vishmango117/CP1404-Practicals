from Car import Car

class GasGuzzler(Car):
    def __init__(self, name, fuel, fuel_consumption_ratio):
        super().__init__(name, fuel)
        self.fuel_consumption_ratio = fuel_consumption_ratio
    

    # In GasGuzzler the fuel consumption is more than usual hence the drive function has to be overridden
    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if (distance) > self.fuel/self.fuel_consumption_ratio:
            distance = self.fuel/self.fuel_consumption_ratio
            self.fuel = 0
            return distance*self.fuel_consumption_ratio
        else:
            self.fuel -= distance
        self.odometer += distance* self.fuel_consumption_ratio
        return distance*self.fuel_consumption_ratio

    def __str__(self):
        return super().__str__() + "Fuel Efficiency Ratio of {} percent compared to original".format(self.fuel_consumption_ratio)
