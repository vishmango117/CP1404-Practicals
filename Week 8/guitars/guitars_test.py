from Guitars import Guitars
from guitar_fileops import read_file, write_file

VERY_LARGE_VALUE = 9999999

# def obj_min_fn(my_obj_list, size):
#     obj_min= Guitars(cost=VERY_LARGE_VALUE)
#     for i in range(size):
#         if(obj_min.__gt__(my_obj_list[i])):
#             obj_min.name=my_obj_list[i].name
#             obj_min.year=my_obj_list[i].year
#             obj_min.cost=my_obj_list[i].cost
#     print(obj_min)
#     return obj_min

def user_input(my_guitars, size):
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    my_guitars.append(Guitars(name, year, cost))
    size+=1
    return  my_guitars, size


def main():
    my_guitars = list()
    (my_guitars, size)= read_file("guitars.csv")
    my_guitars.sort(key = lambda c: c.cost)
    write_file(my_guitars, size, "guitars_final.txt")
    # for i in range(size):
    #     sorted_guitars.append(obj_min_fn(my_guitars, size))
    #     my_guitars.remove(obj_min_fn(my_guitars, size))

if __name__ == "__main__":
    main()