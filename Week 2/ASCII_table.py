# CP1404 Practical 2 
#ASCII Table Generator

LOWER = 33
UPPER = 127


def ascii_table():
    char = input("Enter Character: ")
    print("The ASCII code for {} is {}".format(char,ord(char)))
    char = int(input("Enter character between 33 and 127: "))
    while (not(33 < char < 127)):
        print("Try Again")
        char = int(input("Enter character between 33 and 127: "))
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
    ascii_col_challenge()


if __name__ == "__main__":
    main()