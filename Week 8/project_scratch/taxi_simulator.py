from Taxi import Taxi
from SilverServiceTaxi import SilverServiceTaxi
import copy

# def objectcopy(src_object):
#     dest_object =  



def main():
    taxi_list = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    my_taxi = None
    totalbill = 0
    flag = True
    print("Let's drive!")
    while flag:
        print("Menu:")
        print("q) quit")
        print("c) choose taxi")
        print("d) drive)")
        menuoption = input(">>>")
        if(menuoption == "D" or menuoption == "d"):
            if not(my_taxi in taxi_list):
               my_taxi = taxi_list[0]
            print(my_taxi)
            curr_trip_distance = int(input("Drive how far?"))
            my_taxi.start_fare()
            curr_distance_driven = my_taxi.drive(curr_trip_distance)
            totalbill += my_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(my_taxi.name, my_taxi.get_fare()))
            print("Bill to date : ${:.2f}".format(totalbill))
        
        
        elif(menuoption == "c" or menuoption == "C"):
            print("Taxis available:")
            for i in range(len(taxi_list)):
               print(taxi_list[i])
            taxioption = int(input("Choose Taxi: "))
            my_taxi = taxi_list[taxioption]
            print("Bill to date: ${:.2f}".format(totalbill))
            second_flag = True
            while second_flag:
                if not(0 <= taxioption < len(taxi_list)):
                    print("Invalid Option Try Again..!!")
                else:
                    my_taxi = taxi_list[taxioption]
                    second_flag = False

        elif(menuoption == "q" or menuoption == "Q"):
           print("Total Trip Cost: ${:.2f}".format(totalbill))
           flag = False
        else:
            print("Invalid Menu Choice")
if __name__ == "__main__":
    main()