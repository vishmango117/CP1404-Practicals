#CP1404 Programming II Auto Password Generator
# Can be used for generating tokens of some sort

import random\

SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
VOWELS = "aeiou"
VOWELS_CASE = "AEIOU"
CONSONANTS_CASE = "BCDFGHJKLMNPQRSTVWXYZ"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
def password_generator(size):
    randlist = []
    password = str()
    for i in range(size):
        option = random.randint(0,5)
        if(option == 0):
            randlist.append(random.choice(VOWELS))
        elif(option == 1):
            randlist.append(random.choice(CONSONANTS))
        elif(option == 2):
            randlist.append(random.choice(SPECIAL_CHARACTERS))
        elif(option == 3):
            randlist.append(str(random.randint(0,9)))
        elif(option == 4):
            randlist.append(random.choice(VOWELS_CASE))
        elif(option == 5):
            randlist.append(random.choice(CONSONANTS_CASE))

    password = password.join(randlist)
    return password


def main():
    passwordchecker2() # follows the same as 1st except special and length is from 2 to 6

def passwordchecker2():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH2, "and", MAX_LENGTH2,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    size = int(input("Enter Size: "))
    password = password_generator(size)

    flag = True
    while flag:
        
        while not is_valid_password2(password, size):
            password = password_generator(size)
        
        print("Password Generated is: ",password)
        option = input("Accept(Y/N): ")
        if(option == "Y" or option == "y"):
            flag = False
        elif(option == "N" or option == "n"):
            print("Generating Again Please Wait: ")
            password = password_generator(size)
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))

def is_valid_password2(password, size):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if(char.islower()):
            count_lower += 1
        elif(char.isupper()):
            count_upper += 1
        elif(char.isdigit()):
            count_digit += 1
        elif(char in SPECIAL_CHARACTERS):
            count_special += 1
    if(not(count_digit >0 and count_lower >0 and count_upper>0 and count_special > 0)):
        return False
        
    return True

if __name__ == "__main__":
    main()