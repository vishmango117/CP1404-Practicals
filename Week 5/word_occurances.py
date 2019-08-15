"""
CP1404/CP5632 Practical
"""

from operator import itemgetter


def main():
    text_input = input("Enter Text: ")
    text_list = text_input.split()
    dictionary = {}
    for word in text_list:
        if(word in dictionary):
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    max_length = max(len(key) for key in dictionary)
    for key, value in sorted(dictionary.items(), key=itemgetter(1)):
        print("{} : {}".format(key, value))
        print("{:{}} : {}".format(key, max_length-len(key), value))


if __name__ == "__main__":
    main()
