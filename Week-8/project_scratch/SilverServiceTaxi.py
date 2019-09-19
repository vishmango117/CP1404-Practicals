from Taxi import Taxi

class SilverServiceTaxi(Taxi):
    
    def __init__(self,name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.50

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of $4.50".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)


