from Person import Person

def person_add(userlist):
    fname = input("Enter your First Name: ")
    lname = input("Enter your Last Name: ")
    age = int(input("Enter your age: "))
    userlist.append(Person(fname,lname,age))



def main():
    userlist = []
    flag = True
    while flag:
        option=input("Add Person.?")
        if(option == "y" or option == "Y"):
            person_add(userlist)
        else:
            flag = False
    for i in len(userlist):
        print(userlist[i])


if __name__ == "__main__":
    main()