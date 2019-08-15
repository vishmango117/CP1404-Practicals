

def main():
    size = int(input("Enter Size: "))
    names, dates_of_birth = [], []
    for i in range(size):
        names.append(input("Enter Name: "))
        dates_of_birth.append(input("Enter DOB(DD/MM/YYYY): "))
    dictionary = dict()
    for i in range(len(dates_of_birth)):
        user_date_list = dates_of_birth[i].split("/")
        user_date_list2 = []
        for index in range(0, len(user_date_list)):
            user_date_list2.append(int(user_date_list[index]))
        user_date_list2 = tuple(user_date_list2)
        dictionary[names[i]] = user_date_list2
    print(dictionary)

if __name__ == "__main__":
    main()
