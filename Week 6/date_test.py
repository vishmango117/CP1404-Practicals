from Date import Date
import datetime

def main():
    curr_date = datetime.datetime.today().strftime('%m/%d/%y').split('/')
    mydate = Date(curr_date[1],curr_date[0],curr_date[2])
    print(mydate)
    








if __name__ == "__main__":
    main()