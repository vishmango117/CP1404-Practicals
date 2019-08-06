""" Program to Calculate and displays a user's bonus based on sales
If sales are under 1000 user get 10% bonus if sales are over 1000 bonus """

flag = True
sales = float(input("Enter Sales: $"))
while sales>0:
    if(sales < 1000):
        bonus = 0.1 * sales
    elif(sales >= 1000):
        bonus = 0.15 * sales
    print("Sales,Bonus",sales,bonus)
    sales = float(input("Enter Sales: $"))

