from Taxi import Taxi

def main():
    mytaxi = Taxi("Crown Victoria", 100)
    mytaxi.drive(40)
    print("Taxi Information\n {}\n Current Fare: ${}".format(mytaxi, mytaxi.get_fare()))
    mytaxi.start_fare()
    print("Taxi Information\n {}\n Current Fare: ${}".format(mytaxi, mytaxi.get_fare()))
if __name__ == "__main__":
    main()