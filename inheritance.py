class Person:
    #class attribute
    number_of_people = 0 
    def __init__(self, name):
        self.name = name 
        Person.add_people()
    #class method     
    @classmethod
    def no_of_people(cls):
        return cls.number_of_people
    #class method 
    @classmethod   
    def add_people(cls):
        cls.number_of_people += 1
#Instantiating a person object       
p1 = Person("Cisco")
p2 = Person("Mel")
print(Person.no_of_people())

    
    