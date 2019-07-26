# CP1404 Practical 2 
#ASCII Table


char = input("Enter Character: ")
print("The ASCII code for {} is {}".format(char,ord(char)))
char = int(input("Enter character between 33 and 127: "))
while (not(33 < char < 127)):
    print("Try Again")
    char = int(input("Enter character between 33 and 127: "))
print("The character for {} is {}".format(char,chr(char)))