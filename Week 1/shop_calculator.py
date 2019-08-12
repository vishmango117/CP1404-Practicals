#CP1404 WEEK 1 PRACTICALS SHOP CALCULATOR

total = 0
size = int(input("Enter Number of Items: "))
while(size <0):
    print("Invalid Size")
    size = int(input("Enter Number of Items: "))
for i in range(size):
    total += float(input("Price of item: "))

if(total > 100):
    print("Total price for Items is ${:.2f}".format(0.9*total))
else:
    print("Total price for Items is ${:.2f}".format(total))
