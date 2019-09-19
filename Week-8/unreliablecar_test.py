from UnreliableCar import UnreliableCar

def main():
    my_shittycar = UnreliableCar("Crown Victoria",100,50)
    my_shittycar.drive(40)
    print("Car Information\n {}".format(my_shittycar))
    my_shittycar.drive(30)
    print("Car Information\n {}".format(my_shittycar))
if __name__ == "__main__":
    main()
