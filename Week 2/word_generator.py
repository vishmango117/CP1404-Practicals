"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#word_format = input("Enter Word Format: ")
size = random.randint(1,10)
randlist=[]
word_format = ''
print(size)
for i in range(size):
    option = random.randint(0,1)
    print(option)
    if(option == 0):
        randlist.append(random.choice(VOWELS))
        print(randlist)
    elif(option == 1):
        randlist.append(random.choice(CONSONANTS))
word_format = word_format.join(randlist)
word_format = word_format.lower()
word = ""
for kind in word_format:
    if kind == "#":
        word += random.choice(VOWELS)
    elif kind == "%":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)