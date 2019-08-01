MIN_LENGTH = 7

def password_checker():
    password = input("Enter Password (should be 7 characters or more")
    while (len(password) < 7):
        print("Try Again")
        password = input("Enter Password (should be 7 characters or more")
    return password

def main():
   password = password_checker()
   print("*"*len(password))

if __name__ == "__main__":
    main()