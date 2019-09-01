from car import Car

def integer_validation(string):
    while True:
        try:
            value = int(input(string))
            if(value <= 0):
                print("Value cannot be negative")
            else:
                return value
        except ValueError:
            print("Invalid Value")




def menu(mycar):
    while True:
        print(mycar)
        print("Menu:")
        print("d) drive")
        print("r) refuel")
        print("q) quit)")
        menuoption = input(">>>")
        if(menuoption == "D" or menuoption == "d"):
            distance = integer_validation("How many km do you wish to drive? ")
            covered = mycar.drive(distance)
            print("The Car covered {} km".format(covered))
        elif(menuoption == "r" or menuoption == "R"):
            refuel_amount = integer_validation("Enter how much fuel you want to refuel")
            mycar.add_fuel(refuel_amount)
        elif(menuoption == "q" or menuoption == "Q"):
            print("Goodbye {}'s driver.".format(mycar.name))
            break
        else:
            print("Invalid Menu Choice")
    return mycar

def main():
    print("Gentleman start your engines")
    mycar = Car(input("Enter Your Car Name:"))
    menu(mycar)

if __name__ == "__main__":
    main()
    