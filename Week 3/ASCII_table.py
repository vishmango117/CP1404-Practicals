# CP1404 Practical 2 
#ASCII Table Generator

LOWER = 33
UPPER = 127

def valid_number():
    flag = True
    number = -1
    while flag:
        try:
            number = int(input("Enter number between 10 and 50: "))
            if (not(10 < number < 50)):
                print("Please enter valid number !")
            else:
                flag = False
        except ValueError:
            print("Please enter valid number !")
    return number


def ascii_table():
    char = valid_number()
    if(char == -1):
        print("Invalid")
    else:
        print("The character for {} is {}".format(char,chr(char)))

def ascii_col_challenge():
    cols = int(input("Enter Numbers of rows to print: "))
    rows = ((UPPER - LOWER) + 1) // cols
    base = LOWER
    for i in range(rows):
        for j in range(cols):
            print("{:6} {:>2}".format(base,chr(base)), end = '')
            base +=1
        print()

def main():
    ascii_table()


if __name__ == "__main__":
    main()