"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH2 = 2
MAX_LENGTH2 = 6
MIN_LENGTH1 = 5
MAX_LENGTH1 = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    passwordchecker1() # Follows the Criteria of 1 lower, 1 upper, 1 special, 1 digit and length from 5 to 15 
    passwordchecker2() # follows the same as 1st except special and length is from 2 to 6

def passwordchecker2():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH2, "and", MAX_LENGTH2,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    password = input("> ")
    while not is_valid_password2(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))

def passwordchecker1():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH1, "and", MAX_LENGTH1,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password1(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password1(password):
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
    if(not(count_digit >0 and count_lower >0 and count_upper>0 and count_special>0 and (5<=len(password)<=15))):
        return False
        
    return True

def is_valid_password2(password):
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
    if(not(count_digit >0 and count_lower >0 and count_upper>0 and count_special == 0 and (2<=len(password)<=6))):
        return False
        
    return True


if __name__ == "__main__":
    main()