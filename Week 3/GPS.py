#Gopher Population Simulator not Global Positioning System
GOPHER_START = 1000
import random
def main():
    population = GOPHER_START
    print("Starting Population", GOPHER_START)
    print("Year 1")
    for i in range(2,11):
        rand_gen = (random.randint(10,20))/100
        rand_loss = (random.randint(5,25))/100
        print("{} gophers were born. {} died".format(int(rand_gen*population),int(rand_loss*population)))
        population -= population*(rand_gen - rand_loss)
        print("Population:",int(population))
        print("Year",i,"\n")

if __name__ == "__main__":
    main()
