

cache_string = []
repeated_string = []


while True:
    user_input = input("Enter String:")
    if(user_input == ""):
        break

    if(user_input in cache_string):
        repeated_string.append(user_input)
    else:
        cache_string.append(user_input)

if(not(repeated_string)):
    print("No repeated strings entered")
else:
    print(repeated_string)