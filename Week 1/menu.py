flag = True
name = (input("Enter Name: "))
while flag:
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    menuoption = input()
    if(menuoption == "H" or menuoption == "h"):
        print("Hello",name)
    elif(menuoption == "G" or menuoption == "g"):
        print("Goodbye",name)
    elif(menuoption == "Q" or menuoption == "q"):
        print("Finished.")
        flag = False
    else:
        print("Invalid Choice")
