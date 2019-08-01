"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
CONSTANT_CHECK="cv"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def is_valid_format(word_format):
    counter = 0
    for char in word_format:
        if(not (char in CONSTANT_CHECK)):
            break
        else:
            counter +=1
    if(counter == len(word_format)):
        flag = False
    else:
        print("Try Again")

def main():
    flag = True
    while flag:
        word_format = input("Enter Word Format: ")
        counter = 0
        for char in word_format:
            if(not (char in CONSTANT_CHECK)):
                break
            else:
                counter +=1
        if(counter == len(word_format)):
            flag = False
        else:
            print("Try Again")
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)

if __name__ == "__main__":
    main()