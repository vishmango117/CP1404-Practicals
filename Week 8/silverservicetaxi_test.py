from SilverServiceTaxi import SilverServiceTaxi

def main():
    total_bill = 0
    my_fancy_taxi = SilverServiceTaxi('myfancycar', 100, 2)
    my_fancy_taxi.drive(18)
    print("Taxi Information\n {}\n Current Fare: ${:.2f}".format(my_fancy_taxi, round(my_fancy_taxi.get_fare(), 1)))


if __name__ == "__main__":
    main()