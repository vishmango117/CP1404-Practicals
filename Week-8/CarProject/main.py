from UnreliableCar import UnreliableCar
from GasGuzzler import GasGuzzler
from Bomb import Bomb
from EcoTaxi import EcoTaxi

def main_eco():
    my_eco_taxi = EcoTaxi("Prius", 100, 0.3)
    print("Car Information\n {}".format(my_eco_taxi))
    my_eco_taxi.start_fare()
    my_eco_taxi.drive(30)
    my_eco_taxi.get_fare()
    print("Car Information\n {}".format(my_eco_taxi))
    my_eco_taxi.drive(30)
    print("Fare Cost: ${}".format(my_eco_taxi.get_fare()))


def main_unreliable():
    my_shittycar = UnreliableCar("Crown Victoria",100,50)
    my_shittycar.drive(40)
    print("Car Information\n {}".format(my_shittycar))
    my_shittycar.drive(30)
    print("Car Information\n {}".format(my_shittycar))

def main_guzzler():
    my_ineffecient_car = GasGuzzler("Toyota Corolla 1995", 100, 0.5)
    print("Car Information\n {}".format(my_ineffecient_car))
    my_ineffecient_car.drive(20)
    print("Car Information\n {}".format(my_ineffecient_car))

def main():
    main_unreliable()
    main_guzzler()
    main_eco()

if __name__ == "__main__":
    main()
