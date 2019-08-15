user_name = input("Enter Name: ")
user_date = input("Enter Date(DD/MM/YYYY): ")

dictionary = {}
user_date_list = user_date.split("/")
user_date_list2 = []
for index in range(0, len(user_date_list)):
    user_date_list2.append(int(user_date_list[index]))
user_date_list2 = tuple(user_date_list2)
dictionary[user_name] = user_date_list2
print(dictionary)
