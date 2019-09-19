CURR_YEAR = 2019
CURR_MONTH = 8
CURR_DATE = 29

from datetime import datetime

class Guitars:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost
    
    def __str__(self):
        if(self.is_vintage()):
            return "{} ({}), worth $ {:.2f} (vintage)".format(self.name, self.year, self.cost)
        else:
             return "{} ({}) : worth ${:.2f}".format(self.name, self.year, self.cost)
    
    def __gt__(self, other):
        return self.cost > other.cost
        


    def get_age(self):
       
        return abs(self.year-datetime.today().year)
    
    def is_vintage(self):
        if(self.get_age()>=50):
            return True
        return False


