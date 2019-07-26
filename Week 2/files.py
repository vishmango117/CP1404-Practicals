
def name_write():
    name = input("Enter Name: ")
    fp = open('name.txt','w')
    print(name,file=fp)
    fp.close()

def name_read():
    fp = open('name.txt','r')
    name = fp.readline()
    print("Your Name is:",name)
    fp.close()

def read_then_sum_then_write():
    sum = 0
    fp = open('numbers.txt','r')
    data = fp.readlines()
    for numbers in data:
        sum += int(numbers)
    print(sum)
    fp.close()

def main():
    #name_write()
    #name_read()
    read_then_sum_then_write()

if __name__ == "__main__":
    main()
