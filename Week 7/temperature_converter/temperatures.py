"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def celsius_to_fahrenheit(celsius):
    #celsius = float(input("Celsius: "))
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    #fahrenheit = float(input("Farenheit "))
    return 5 / 9 * (fahrenheit - 32)

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    flag = True
    while flag:
        print(MENU)
        choice = input(">>> ").upper()
        if (choice == "Q" or choice == "q"):
            flag = False
        elif (choice == "C" or choice == "c"): #made it case insensitive
            print("Result: {:.2f} F".format(celsius_to_fahrenheit()))
        elif (choice == "F" or choice == "f"): # made it case insensitive
            print("Result: {:.2f} C".format(fahrenheit_to_celsius()))
        else:
            print("Invalid option")
    print("Thank you.")

