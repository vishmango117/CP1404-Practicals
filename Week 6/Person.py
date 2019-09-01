class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def __str__(self):
        return "Personal Information\nFirst Name: {}\nLast Name: {}\nAge: {}\n".format(self.fname, self.lname, self.age)