"""
CP1404/CP5632 Practical
"""


def main():
    colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
               "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
               "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
               "aquamarine4": "#458b74"}
    user_input = input("Enter Colour name:")
    print("Colour code is", colours[user_input])


if __name__ == "__main__":
    main()
