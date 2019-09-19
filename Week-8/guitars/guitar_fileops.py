from Guitars import Guitars
import csv

def read_file(filename):
    """ read_file(): FUNCTION DESIGNED TO READ CSV FILES
    AND SET THEM INTO DICTIONARY
    SORTING IS DONE BASED ON THE LIST INSIDE DICTIONARY
    PARAMS: FILENAME(STRING)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    destination = []
    size = 0
    # OPEN FILE
    try:
        file_read = open(filename, 'r')
    except FileNotFoundError:
        print("File Not Found")
        exit()
    file_row = csv.reader(file_read, delimiter=',')
    
    for data in file_row:
        #print(data[0], data[1], data[2])
        destination.append(Guitars(data[0],data[1],data[2]))
        destination[size].cost = float(destination[size].cost)
        destination[size].year = int(destination[size].year)
        size+=1
    
    file_read.close()
    return (destination, size)

def write_file(dictionary, size, filename):
    """ write_file(): FUNCTION TO WRITE TO CSV FILE
    WRITING IS DONE WHEN PROGRAM IS QUITTED OR ERR(KEYBOARD INTERRUPT)
    PARAMS: DICTIONARY(DICT), SIZE(INT), FILENAME(STRING)
    RETURN VALUE: NO VALUES ARE RETURNED"""

    # START OF FUNCTION
    fp = open(filename, 'w+')
    for i in range(0, size):
        print("{},{},{}".format(dictionary[i].name, dictionary[i].year, dictionary[i].cost, file=fp))
    print("{} places saved to {}".format(size, filename))
    fp.close()
