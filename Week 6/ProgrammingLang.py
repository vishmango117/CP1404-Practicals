class ProgrammingLang:
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year
    
    
    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection,self.year)


    def isdynamic(self):
        if(self.typing == "Dynamic"):
           return self.field
        else:
            return ""
        
           


