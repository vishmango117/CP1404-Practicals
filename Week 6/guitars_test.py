from Guitars import Guitars

def user_input(my_guitars, size):
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    my_guitars.append(Guitars(name, year, cost))
    size+=1
    return  my_guitars, size

def custom_print(my_guitars, size):
    print("These are my guitars\n.... snip ....")
    for index in range(size):
        print("Guitar {}: ".format(index+1), end = ' ')
        print(my_guitars[index])

def main():
    my_guitars = list()
    my_guitars.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
    my_guitars.append(Guitars("Stradovarius", 2013,450.54))
    (my_guitars, size) = user_input(my_guitars,len(my_guitars))
    for i in range(size):
        print("{} get_age() - Expected {} got 97".format(my_guitars[i].name, my_guitars[i].get_age()))
        print("{} is_vintage() - Expected {} got True".format(my_guitars[i].name, my_guitars[i].is_vintage()))
    custom_print(my_guitars, size)

if __name__ == "__main__":
    main()