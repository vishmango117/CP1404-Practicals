import csv

def read_file(filename):
    """ read_file(): FUNCTION DESIGNED TO READ CSV FILES
    AND SET THEM INTO DICTIONARY
    SORTING IS DONE BASED ON THE LIST INSIDE DICTIONARY
    PARAMS: FILENAME(STRING)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    destination = dict()
    size = 0
    unvisited_counter = 0
    # OPEN FILE
    try:
        file_read = open(filename, 'r')
    except FileNotFoundError:
        print("File Not Found")
        exit()
    file_row = csv.reader(file_read, delimiter=',')
    for data in file_row:
        print(data)
    file_read.close()

    # typecasting priority to int
    for i in range(size):
        destination[i][2] = int(destination[i][2])

    return (destination, size, unvisited_counter)

def write_file(dictionary, size, filename):
    """ write_file(): FUNCTION TO WRITE TO CSV FILE
    WRITING IS DONE WHEN PROGRAM IS QUITTED OR ERR(KEYBOARD INTERRUPT)
    PARAMS: DICTIONARY(DICT), SIZE(INT), FILENAME(STRING)
    RETURN VALUE: NO VALUES ARE RETURNED"""

    # START OF FUNCTION
    fp = open(filename, 'w')
    for i in range(size):
        print("{},{},{},{}".format(dictionary[i][0], dictionary[i][1], dictionary[i][2], file=fp))
    print("{} places saved to {}".format(size, filename))
    fp.close()


def main():
    read_file("guitars.csv")



if __name__ == "__main__":
    main()