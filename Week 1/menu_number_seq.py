#CP1404 Week 1 Menu Number Generation

def print_evenno():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    for x in range(y):
        if(x%2 == 0):
            print(x)

def print_oddno():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    for x in range(y):
        if(x%2 !=0):
            print(x)

def print_squares():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    for x in range(y):
        print(x**2)

# Main Function
def main():
    flag = True
    while flag:
        print("(E) Show the even numbers from x to y")
        print("(O) Show the odd numbers from x to y")
        print("(S) Show the squares from x to y")
        print("(Q) Exit the program")
        menuoption = input()
        if(menuoption == "E" or menuoption == "e"):
            print_evenno()
        elif(menuoption == "O" or menuoption == "o"):
            print_oddno()
        elif(menuoption == "S" or menuoption == "s"):
            print_squares()
        elif(menuoption == "Q" or menuoption == "q"):
            print("Finished.")
            flag = False
        else:
            print("Invalid Choice")


# Calling Main Function
if __name__ == "__main__":
    main()