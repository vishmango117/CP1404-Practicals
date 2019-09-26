from Taxi import Taxi

class EcoTaxi(Taxi):
    def __init__(self,name, fuel,discount):
        super().__init__(name, fuel)
        self.discount = discount
        self.fuel_efficient = 0.5
    
    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.odometer *= 0.5
        self.fuel += (100-self.fuel)*0.5
        self.current_fare_distance += distance_driven
        return distance_driven

    def get_fare(self):
        """Return the price for the taxi trip."""
        return float(super().get_fare() * (1-self.discount))

    def __str__(self):
        return super().__str__()

    